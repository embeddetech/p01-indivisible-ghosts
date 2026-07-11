import numpy as np
from scipy.linalg import expm, sqrtm, eig
 
np.set_printoptions(precision=4, suppress=True)
 
def build_H(r, theta, s):
    return np.array([[r*np.exp(1j*theta), s],
                     [s,                    r*np.exp(-1j*theta)]], dtype=complex)
 
P = np.array([[0,1],[1,0]], dtype=complex)   # parity
def PT_check(H):
    # PT symmetry: P H* P == H
    return np.allclose(P @ H.conj() @ P, H)
 
def biorthogonal_metric(H):
    """Canonical metric eta = (V^{-1})^dagger (V^{-1}) from right-eigvec matrix V."""
    E, V = eig(H)
    Vinv = np.linalg.inv(V)
    eta = Vinv.conj().T @ Vinv
    eta = 0.5*(eta + eta.conj().T)   # symmetrize numerical noise
    return E, V, eta
 
def all_hermitian_intertwiners(H):
    """Find Hermitian eta solving H^dag eta - eta H = 0. Return basis + signatures."""
    # Hermitian 2x2 basis: I, sx, sy, sz
    I=np.eye(2,dtype=complex); sx=np.array([[0,1],[1,0]],dtype=complex)
    sy=np.array([[0,-1j],[1j,0]],dtype=complex); sz=np.array([[1,0],[0,-1]],dtype=complex)
    basis=[I,sx,sy,sz]
    # map eta -> H^dag eta - eta H  (anti-Hermitian => expand in i*{I,sx,sy,sz})
    rows=[]
    Hd=H.conj().T
    for B in basis:
        M = Hd@B - B@H
        # components along i*basis (real coeffs)
        comps=[np.real(np.trace((1j*C).conj().T @ M))/2 for C in basis]
        rows.append(comps)
    A=np.array(rows).T   # 4x4 : A @ coeff = 0
    # nullspace
    u,sv,vh=np.linalg.svd(A)
    null=vh[np.abs(sv)<1e-9] if np.any(np.abs(sv)<1e-9) else vh[[-1]]
    # also include near-zero singular directions
    tol=1e-8
    null=vh[[i for i in range(4) if sv[i]<tol]] if np.any(sv<tol) else vh[[3]]
    sols=[]
    for c in null:
        eta=sum(ci*Bi for ci,Bi in zip(c,basis))
        eta=0.5*(eta+eta.conj().T)
        ev=np.linalg.eigvalsh(eta)
        sols.append((eta,ev))
    return sols
 
def col_sums(G):
    return G.sum(axis=0).real
 
def report(label, r, theta, s, t=1.3):
    print("="*70)
    print(f"{label}:  r={r}, theta={theta:.4f}, s={s}")
    H=build_H(r,theta,s)
    print("PT-symmetric:", PT_check(H))
    E,V,eta=biorthogonal_metric(H)
    Es,_=eig(H)
    print("eigenvalues:", np.round(np.sort_complex(Es),4))
    real_spec = np.allclose(Es.imag,0,atol=1e-9)
    print("real spectrum (PT-unbroken):", real_spec)
 
    U=expm(-1j*H*t)
    # --- naive Barandes ---
    G_naive=np.abs(U)**2
    print("\nNaive Gamma=|U|^2 column sums:", np.round(col_sums(G_naive),4),
          " (want [1,1])")
 
    # --- metric intertwining check ---
    print("H^dag eta - eta H  ~0 ?", np.allclose(H.conj().T@eta-eta@H,0,atol=1e-8),
          "| eta eigenvalues:", np.round(np.linalg.eigvalsh(eta),4),
          "| eta positive-definite:", np.all(np.linalg.eigvalsh(eta)>1e-9))
 
    if real_spec:
        rho=sqrtm(eta)              # eta^{1/2}, positive Hermitian
        rho_inv=np.linalg.inv(rho)
        h=rho@H@rho_inv
        print("h=eta^{1/2} H eta^{-1/2} Hermitian:", np.allclose(h,h.conj().T,atol=1e-8))
        u=rho@U@rho_inv
        print("u unitary:", np.allclose(u@u.conj().T,np.eye(2),atol=1e-8))
        G_metric=np.abs(u)**2
        print("Metric-corrected Gamma=|eta^{1/2} U eta^{-1/2}|^2:")
        print(np.round(G_metric,4))
        print("  column sums:", np.round(col_sums(G_metric),4),
              "| entries>=0:", np.all(G_metric>=-1e-12),
              "| doubly-stochastic:", np.allclose(col_sums(G_metric),1)
                                        and np.allclose(G_metric.sum(axis=1),1))
        # indivisibility: Gamma(2t) vs Gamma(t)^2
        u2=rho@expm(-1j*H*2*t)@rho_inv
        G2=np.abs(u2)**2
        print("  indivisible? ||Gamma(2t) - Gamma(t)^2|| =",
              round(np.linalg.norm(G2-G_metric@G_metric),4), "(>0 => non-Markovian)")
    else:
        print("\n-> No positive-definite metric exists. Hermitian intertwiners H^dag eta = eta H:")
        for eta_s,ev in all_hermitian_intertwiners(H):
            print("   intertwiner eigenvalues:", np.round(ev,4),
                  "=> signature indefinite:", (ev[0]*ev[-1]<0))
        # show blow-up
        norms=[np.linalg.norm(expm(-1j*H*tt)) for tt in [0.5,1,2,4,8]]
        print("   ||U(t)|| at t=0.5,1,2,4,8:", np.round(norms,3), "(exponential growth)")
        cs=[col_sums(np.abs(expm(-1j*H*tt))**2) for tt in [1,2,4]]
        print("   naive |U|^2 col sums at t=1,2,4:", [list(np.round(c,3)) for c in cs])
 
r,theta=1.0,np.pi/4
report("UNBROKEN PHASE", r, theta, s=1.0)
report("BROKEN PHASE",   r, theta, s=0.5)