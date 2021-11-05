"""
Гипотетическая модель экономики:
C = a_1 + b_11 * Y + b_12 * J
J = a_2 + b_21 * Y_t-1
T = a_3 + b_31 * Y
Y = C + J + G

C - совокупное потребление в период t
Y - совокупный доход в период t
J - инвестиции в период t
T - налог в период t
G - государственные доходы в период t
"""
from pathlib import Path

from sympy import Matrix, solve, Eq

from . import utils

# =========================== ДАНО ===========================

endos = 'C J T Y'
endos = utils.get_symbols_dict(endos)

predeters = 'Y_t-1 G'
predeters = utils.get_symbols_dict(predeters)

params = 'a_1 a_2 a_3 b_11 b_12 b_21 b_31'
params = utils.get_symbols_dict(params)

# =========================== СТРУКТУРНАЯ ФОРМА (система) ===========================

eq_system = [
    Eq(endos['C'],
       params['a_1'] + params['b_11'] * endos['Y'] + params['b_12'] * endos['J']),
    Eq(endos['J'],
       params['a_2'] + params['b_21'] * predeters['Y_t-1']),
    Eq(endos['T'],
       params['a_3'] + params['b_31'] * endos['Y']),
    Eq(endos['Y'],
       endos['C'] + endos['J'] + predeters['G']),
]

# =========================== ПРИВЕДЕННАЯ ФОРМА (система) ===========================

reduced_form_system = solve(eq_system, *endos.values())

# =========================== КОМПОНЕНТЫ ФОРМЫ (матрица) ===========================

Y = utils.create_endos_v(endos)
X = utils.create_predeters_v([1], predeters)

# матрица коэффициентов при ЭНДОГЕННЫХ переменных
A = Matrix([
    [1, -params['b_12'], 0, -params['b_11']],
    [0, 1, 0, 0],
    [0, 0, 1, -params['b_31']],
    [-1, -1, 0, 1],
])

# матрица коэффициентов при ПРЕДОПРЕДЕЛЕННЫХ (и мнимых) переменных
B = Matrix([
    [-params['a_1'], 0, 0],
    [-params['a_2'], -params['b_21'], 0],
    [-params['a_3'], 0, 0],
    [0, 0, -1],
])

U = Matrix([
    [0],
    [0],
    [0],
    [0],
])

# =========================== ПРИВЕДЕННАЯ ФОРМА (матрица) ===========================

M = utils.calc_M(A, B)
reduced_form_matrix = utils.get_reduced_form(X, Y, A, M, U)

# =========================== ПРОВЕРКА ===========================

assert reduced_form_system == solve(reduced_form_matrix, *endos.values())

# =========================== СОХРАНЕНИЕ PNG ===========================

if __name__ == '__main__':
    OUTPUT_FOLDER = f'../resources/{Path(__file__).stem}'

    utils.save_reduced_system(reduced_form_system, OUTPUT_FOLDER)

    utils.save_components(OUTPUT_FOLDER, A=A, Y=Y, B=B, X=X, U=U)
    utils.save_reduced_matrix(reduced_form_matrix, OUTPUT_FOLDER, dvioptions=['-T', '20.5cm,4.5cm', '-O', '3cm,4cm'])
