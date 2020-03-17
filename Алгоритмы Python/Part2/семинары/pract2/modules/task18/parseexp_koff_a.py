from utils import is_digital
def get(input_str):
    symbols = 1
    return_flag = False
    while return_flag == False:

        index_a = input_str[:symbols]
        if is_digital(index_a) == False and symbols != 1:
            return_flag = True

        symbols += 1

    index_a = input_str[:symbols - 2]
    return index_a