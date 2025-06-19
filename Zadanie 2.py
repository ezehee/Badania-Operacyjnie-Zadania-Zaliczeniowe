from scipy.optimize import linprog

# Zadanie z Kolokwium 2024 Wersja 4
# Funkcja celu: -x1 - 2x2 + 2x3 -> MIN
# Ograniczenia:
# 2x1 - x2 + x3 = 10
# x1 - x2 = 2
# xj >= 0 dla j = 1, 2, 3

# Dane
dane_funkcji_celu = [-1, -2, 2]
macierz_rownan = [
    [2, -1, 1],
    [1, -1, 0]
]
wartosci_rownan = [
    10,
    2
]

# Ograniczenia zmiennych decyzyjnych
ograniczenia = [(0, float('inf'))] * 3

# Rozwiazywanie problemu optymalizacji
wynik = linprog(
    c=dane_funkcji_celu,
    A_eq=macierz_rownan,
    b_eq=wartosci_rownan,
    bounds=ograniczenia,
    method="highs"
)

# Wynik
if wynik.success:
    print("Optymalizacja zakonczona sukcesem!")
    print(f"Minimalna wartosc funkcji celu (Zmin): {wynik.fun}")
    print(f"Zmienne decyzyjne: {wynik.x}")
else:
    print("Optymalizacja nie powiodla sie.")
    print(f"Powod: {wynik.message}")
