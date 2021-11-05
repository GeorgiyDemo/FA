from sympy import Symbol, Matrix, Eq, MatAdd, MatMul, preview, S, zeros


def get_symbols_dict(s: str) -> dict:
    return {i: Symbol(i) for i in s.split(' ')}


def create_endos_v(endos: dict) -> Matrix:
    """
    Вектор ЭНДОГЕННЫХ переменных
    """
    return Matrix([[i] for i in endos.values()])


def create_predeters_v(pseudos: list, predeters: dict) -> Matrix:
    """
    Вектор ПРЕДОПРЕДЕЛЕННЫХ (и мнимых) переменных
    """
    return Matrix([[i] for i in [*pseudos, *predeters.values()]])


def calc_M(A: Matrix, B: Matrix) -> Matrix:  # noqa
    """
    M = -A ** (-1) * B
    """
    return -A.inv() * B


def get_reduced_form(X: Matrix, Y: Matrix, A: Matrix, M: Matrix, U: Matrix) -> Eq:  # noqa
    if zeros(*U.shape) == U:
        res = MatMul(M, X)
    else:
        res = MatAdd(MatMul(M, X), MatMul(A.inv(), U))
    return Eq(Y, res, evaluate=False)


def save_components(path: str, **kwargs):
    for k, v in kwargs.items():
        eq = Eq(S(k), v, evaluate=False)
        preview(eq, output='png', viewer='file', filename=f'{path}/{k}.png', euler=False)


def save_reduced_matrix(reduced_form, path: str, dvioptions=None):
    preview(
        reduced_form,
        output='png',
        viewer='file',
        filename=f'{path}/0_reduced_form_matrix.png',
        euler=False,
        dvioptions=dvioptions
    )


def save_reduced_system(reduced_form, path: str, dvioptions=None):
    preview(
        reduced_form,
        output='png',
        viewer='file',
        filename=f'{path}/0_reduced_form_system.png',
        euler=False,
        dvioptions=dvioptions
    )
