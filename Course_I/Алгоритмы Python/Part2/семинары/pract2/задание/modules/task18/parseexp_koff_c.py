from .utils import is_digital


def get(input_str):
    symbols = input_str.rindex("=")
    buf_index_c = input_str[:symbols]
    symbols = 1
    return_flag = False
    while return_flag == False:
        index_c = buf_index_c[symbols:]
        if is_digital(index_c) == True:
            return_flag = True
        symbols += 1
    return index_c
