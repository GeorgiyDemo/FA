"""
Модель денежного и товарного рынков:
R = a_1 + b_12 * Y + b_14 * M               (1)
Y = a_2 + b_21 * R + b_23 * I + b_25 * G    (2)
I = a_3 + b_31 * R                          (3)

R - процентные ставки
Y - реальный ВВП
M - денежная масса
I - внутренние инвестиции
G - реальные государственные расходы

(1) - f денежного рынка
(2) - f товарного рынка
(3) - f инвестиций
"""
from pathlib import Path

from sympy import Matrix, solve, Eq

from . import utils

# =========================== ДАНО ===========================

endos = 'R Y I'
endos = utils.get_symbols_dict(endos)

predeters = 'M G'
predeters = utils.get_symbols_dict(predeters)

params = 'a_1 a_2 a_3 b_12 b_14 b_21 b_23 b_25 b_31'
params = utils.get_symbols_dict(params)

# =========================== СТРУКТУРНАЯ ФОРМА (система) ===========================

eq_system = [
    Eq(endos['R'],
       params['a_1'] + params['b_12'] * endos['Y'] + params['b_14'] * predeters['M']),
    Eq(endos['Y'],
       params['a_2'] + params['b_21'] * endos['R'] + params['b_23'] * endos['I'] + params['b_25'] * predeters['G']),
    Eq(endos['I'],
       params['a_3'] + params['b_31'] * endos['R']),
]

# =========================== ПРИВЕДЕННАЯ ФОРМА (система) ===========================

reduced_form_system = solve(eq_system, *endos.values())

# =========================== КОМПОНЕНТЫ ФОРМЫ (матрица) ===========================

Y = utils.create_endos_v(endos)
X = utils.create_predeters_v([1], predeters)

# матрица коэффициентов при ЭНДОГЕННЫХ переменных
A = Matrix([
    [1, -params['b_12'], 0],
    [-params['b_21'], 1, -params['b_23']],
    [-params['b_31'], 0, 1]
])

# матрица коэффициентов при ПРЕДОПРЕДЕЛЕННЫХ (и мнимых) переменных
B = Matrix([
    [-params['a_1'], -params['b_14'], 0],
    [-params['a_2'], 0, -params['b_25']],
    [-params['a_3'], 0, 0],
])

U = Matrix([
    [0],
    [0],
    [0]
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
    utils.save_reduced_matrix(reduced_form_matrix, OUTPUT_FOLDER, dvioptions=['-T', '20.5cm,4.5cm', '-O', '3cm,4cm'])
