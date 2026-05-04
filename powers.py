# Replace the "ANSWER HERE" for your answer
from fontTools.diff.color import ansicolors


def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """
    ans = 1
    for i in range(exp):
        ans = ans * base
    return ans


def sum_of_powers(base, max_exp):
    """
    Retorna la suma de base^0 + base^1 + ... + base^max_exp.
    Debe USAR la funcion power.

    Ejemplo: sum_of_powers(2, 3) -> 15  (1+2+4+8)
    """
    ans = 0
    for i in range(0, max_exp + 1):
        ans = ans + power(base, i)
    return ans
