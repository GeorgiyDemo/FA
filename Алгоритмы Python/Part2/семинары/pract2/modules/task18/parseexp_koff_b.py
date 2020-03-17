from utils import is_digital
def get(input_str):
    symbols = input_str.rindex("x")
    buf_index_b = input_str[:symbols]
    symbols = 1
    return_flag = False
    while return_flag == False:

        index_b = buf_index_b[symbols:]

        if is_digital(index_b) == True:
            return_flag = True

        symbols += 1
    return index_b