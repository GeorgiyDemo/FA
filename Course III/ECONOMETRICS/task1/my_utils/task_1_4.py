"""
Модель корректировки размера дивидендов Линтера:
1) D^*_t = g * P_t
2) D_t - D_t-1 = a + b * (D^*_t - D_t-1) + e_0

P_t - текущая прибыль фирмы после уплаты налогов
D_t - дивиденды, которые фирма выплачивает своим акционерам в текущем периоде
D^*_t - целевые дивиденды
g - доля прибыли, направляемая на дивиденды
"""

from pathlib import Path

from sympy import Matrix, solve, Eq

from . import utils

# =========================== ДАНО ===========================

endos = 'D_t D^*_t'
endos = utils.get_symbols_dict(endos)

predeters = 'P_t D_t-1'
predeters = utils.get_symbols_dict(predeters)

params = 'g a b'
params = utils.get_symbols_dict(params)

devs = 'e_0'
devs = utils.get_symbols_dict(devs)

# =========================== СТРУКТУРНАЯ ФОРМА (система) ===========================

eq_system = [
    Eq(endos['D^*_t'],
       params['g'] * predeters['P_t']),
    Eq(endos['D_t'] - predeters['D_t-1'],
       params['a'] + params['b'] * (endos['D^*_t'] - predeters['D_t-1']) + devs['e_0']),
]

# =========================== ПРИВЕДЕННАЯ ФОРМА (система) ===========================

reduced_form_system = solve(eq_system, *endos.values())

# =========================== КОМПОНЕНТЫ ФОРМЫ (матрица) ===========================

Y = utils.create_endos_v(endos)
X = utils.create_predeters_v([1], predeters)

# матрица коэффициентов при ЭНДОГЕННЫХ переменных
A = Matrix([
    [0, 1],
    [1, -params['b']],
])

# матрица коэффициентов при ПРЕДОПРЕДЕЛЕННЫХ (и мнимых) переменных
B = Matrix([
    [0, -params['g'], 0],
    [-params['a'], 0, params['b'] - 1],
])

U = Matrix([
    [0],
    [devs['e_0']],
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
    utils.save_reduced_matrix(reduced_form_matrix, OUTPUT_FOLDER, dvioptions=['-T', '9cm,3cm', '-O', '3cm,3cm'])
