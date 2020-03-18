def display(software_list):
    for software in software_list:
            print(software.software_info() + "\n")

def search(software_list):
    search_flag = False
    print("\n*ПО, которое допустимо использовать на текущую дату*")
    for software in software_list:
        if software.opportunity_detector():
            print(software.software_info() + "\n")
            search_flag = True
    if not search_flag:
        print("ПО не найдено")