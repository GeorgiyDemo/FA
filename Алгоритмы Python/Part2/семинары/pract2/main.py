from modules import *
def main():
    d_selector = {}
    for i in range(1,21):
        
        d_selector[str(i)]=eval("task"+str(i))
    input_str = ""
    while input_str != "0":
        input_str = input("\033[93mВведите номер задания (1-20) или 0 для завершения работы -> \033[0m")
        if input_str in d_selector: d_selector[input_str].main()
if __name__ == "__main__":
    main()