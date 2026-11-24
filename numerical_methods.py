"""Comparaison de méthodes numériques pour résoudre f(x)=0."""
from math import isfinite

def bisection(f, a, b, tol=1e-10, max_iter=10000):
    fa, fb = f(a), f(b)
    if fa == 0: return {"root": a, "iterations": 0, "history": []}
    if fb == 0: return {"root": b, "iterations": 0, "history": []}
    if fa * fb > 0: raise ValueError("f(a) et f(b) doivent être de signes opposés.")
    hist = []
    for k in range(1, max_iter + 1):
        m = (a+b)/2; fm = f(m); hist.append((m, fm))
        if abs(fm) <= tol or (b-a)/2 <= tol:
            return {"root": m, "iterations": k, "history": hist}
        if fa*fm < 0: b, fb = m, fm
        else: a, fa = m, fm
    raise RuntimeError("Nombre maximal d'itérations atteint.")

def false_position(f, a, b, tol=1e-10, max_iter=10000):
    fa, fb = f(a), f(b)
    if fa == 0: return {"root": a, "iterations": 0, "history": []}
    if fb == 0: return {"root": b, "iterations": 0, "history": []}
    if fa*fb > 0: raise ValueError("f(a) et f(b) doivent être de signes opposés.")
    hist = []
    for k in range(1, max_iter+1):
        den = fb-fa
        if den == 0: raise ZeroDivisionError("Dénominateur nul.")
        x = (a*fb-b*fa)/den; fx = f(x); hist.append((x, fx))
        if abs(fx) <= tol: return {"root": x, "iterations": k, "history": hist}
        if fa*fx < 0: b, fb = x, fx
        else: a, fa = x, fx
    raise RuntimeError("Nombre maximal d'itérations atteint.")

def fixed_point(g, x0, tol=1e-10, max_iter=10000):
    x = x0; hist = []
    for k in range(1, max_iter+1):
        xn = g(x)
        if not isfinite(xn): raise ArithmeticError("Itération non finie.")
        hist.append((xn, xn-x))
        if abs(xn-x) <= tol: return {"root": xn, "iterations": k, "history": hist}
        x = xn
    raise RuntimeError("Nombre maximal d'itérations atteint.")

def newton(f, df, x0, tol=1e-10, max_iter=1000):
    x = x0; hist = []
    for k in range(1, max_iter+1):
        d = df(x)
        if abs(d) < 1e-14: raise ZeroDivisionError("Dérivée trop proche de zéro.")
        xn = x-f(x)/d
        if not isfinite(xn): raise ArithmeticError("Itération non finie.")
        fx = f(xn); hist.append((xn, fx))
        if abs(fx) <= tol or abs(xn-x) <= tol:
            return {"root": xn, "iterations": k, "history": hist}
        x = xn
    raise RuntimeError("Nombre maximal d'itérations atteint.")

def main():
    f = lambda x: x**3-x-2
    df = lambda x: 3*x**2-1
    g = lambda x: (x+2)**(1/3)
    methods = [
        ("Dichotomie", bisection(f, 1, 2)),
        ("Fausse position", false_position(f, 1, 2)),
        ("Newton", newton(f, df, 1.5)),
        ("Point fixe", fixed_point(g, 1.5)),
    ]
    print(f"{'Méthode':<19}{'Approximation':>18}{'Itérations':>13}{'Résidu':>14}")
    for name, r in methods:
        print(f"{name:<19}{r['root']:>18.11f}{r['iterations']:>13}{abs(f(r['root'])):>14.2e}")
    try:
        import matplotlib.pyplot as plt
        reference = methods[0][1]["root"]
        for name, r in methods:
            errors = [abs(x-reference) for x, _ in r["history"]]
            if errors: plt.semilogy(range(1, len(errors)+1), errors, marker=".", label=name)
        plt.xlabel("Itération"); plt.ylabel("Écart à l'approximation de référence")
        plt.title("Comparaison de convergence"); plt.grid(True); plt.legend()
        plt.tight_layout(); plt.savefig("convergence.png", dpi=160)
        print("Graphique enregistré dans convergence.png")
    except ImportError:
        print("Pour le graphique : python -m pip install matplotlib")

if __name__ == "__main__": main()
