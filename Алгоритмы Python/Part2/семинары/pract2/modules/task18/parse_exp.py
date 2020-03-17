from .parseexp_koff/koff_a.py import .parseexp_koff/koff_a.py

def parse_exp(self):
        input_str = self.input_str

        # Определяем коэффициент a
        index_a = 

        # Определяем коэффициент b
        symbols = input_str.rindex("x")
        buf_index_b = input_str[:symbols]
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_b = buf_index_b[symbols:]

            if self.is_digital(index_b) == True:
                return_flag = True

            symbols += 1

        # Определяем коэффициент c
        symbols = input_str.rindex("=")
        buf_index_c = input_str[:symbols]
        symbols = 1
        return_flag = False
        while return_flag == False:

            index_c = buf_index_c[symbols:]

            if self.is_digital(index_c) == True:
                return_flag = True

            symbols += 1

        self.index_a = float(index_a)
        self.index_b = float(index_b)
        self.index_c = float(index_c)