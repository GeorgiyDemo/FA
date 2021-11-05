"""
Модель Манделла - Флеминга (IS-LM-BP):
1) Y = C + I + G + NX
2) C = a + b * (Y - T) + e_0, 0 <= b <= 1
3) I = c + d * R + e_1, d < 0
4) L = f + g * Y + h * R + e_2, g > 0, h < 0
5) M = L
6) NX = p + qE + e_3, q < 0
7) CF = r + sR + e_4, s > 0
8) CF + NX = 0
"""

from pathlib import Path

from sympy import Matrix, solve, Eq

from . import utils

# =========================== ДАНО ===========================

endos = 'Y C I NX E R L CF'
endos = utils.get_symbols_dict(endos)

predeters = 'M P G T'
predeters = utils.get_symbols_dict(predeters)

params = 'a b c d f g h p q r s'
params = utils.get_symbols_dict(params)

devs = 'e_0 e_1 e_2 e_3 e_4'
devs = utils.get_symbols_dict(devs)

# =========================== СТРУКТУРНАЯ ФОРМА (система) ===========================

eq_system = [
    Eq(endos['Y'],
       endos['C'] + endos['I'] + predeters['G'] + endos['NX']),
    Eq(endos['C'],
       params['a'] + params['b'] * (endos['Y'] - predeters['T']) + devs['e_0']),
    Eq(endos['I'],
       params['c'] + params['d'] * endos['R'] + devs['e_1']),
    Eq(endos['L'],
       params['f'] + params['g'] * endos['Y'] + params['h'] * endos['R'] + devs['e_2']),
    Eq(predeters['M'],
       endos['L']),
    Eq(endos['NX'],
       params['p'] + params['q'] * endos['E'] + devs['e_3']),
    Eq(endos['CF'],
       params['r'] + params['s'] * endos['R'] + devs['e_4']),
    Eq(0,
       endos['CF'] + endos['NX']),
]

# =========================== ПРИВЕДЕННАЯ ФОРМА (система) ===========================

reduced_form_system = solve(eq_system, *endos.values())

# =========================== КОМПОНЕНТЫ ФОРМЫ (матрица) ===========================

Y = utils.create_endos_v(endos)
X = utils.create_predeters_v([1], predeters)

# матрица коэффициентов при ЭНДОГЕННЫХ переменных
A = Matrix([
    [1, -1, -1, -1, 0, 0, 0, 0],
    [-params['b'], 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, -params['d'], 0, 0],
    [-params['g'], 0, 0, 0, 0, -params['h'], 1, 0],
    [0, 0, 0, 0, 0, 0, -1, 0],
    [0, 0, 0, 1, -params['q'], 0, 0, 0],
    [0, 0, 0, 0, 0, -params['s'], 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
])

# матрица коэффициентов при ПРЕДОПРЕДЕЛЕННЫХ (и мнимых) переменных
B = Matrix([
    [0, 0, 0, -1, 0],
    [-params['a'], 0, 0, 0, params['b']],
    [-params['c'], 0, 0, 0, 0],
    [-params['f'], 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [-params['p'], 0, 0, 0, 0],
    [-params['r'], 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
])

U = Matrix([
    [0],
    [devs['e_0']],
    [devs['e_1']],
    [devs['e_2']],
    [0],
    [devs['e_3']],
    [devs['e_4']],
    [0],
])

# =========================== ПРИВЕДЕННАЯ ФОРМА (матрица) ===========================

M = utils.calc_M(A, B)
reduced_form_matrix = utils.get_reduced_form(X, Y, A, M, U)

# =========================== ПРОВЕРКА ===========================

assert reduced_form_system == solve(reduced_form_matrix, *endos.values())

# =========================== СОХРАНЕНИЕ PNG ===========================

if __name__ == '__main__':
    OUTPUT_FOLDER = f'../resources/{"_".join(Path(__file__).stem.split("_")[-2:])}'

    utils.save_reduced_system(reduced_form_system, OUTPUT_FOLDER)

    utils.save_components(OUTPUT_FOLDER, A=A, Y=Y, B=B, X=X, U=U)
    utils.save_reduced_matrix(reduced_form_matrix, OUTPUT_FOLDER, dvioptions=['-T', '27cm,12cm', '-O', '3cm,4cm'])
