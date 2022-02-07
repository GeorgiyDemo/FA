lst_val = [1, 2, 7, 11, 8, 2]
# создание списка с помощью цикла:
lst_new = []
for el in lst_val:
    lst_new.append(el * 2)

print(lst_new)
# создание аналогичного списка при помощи генератора:
lst_gen = [el * 2 for el in lst_val]
print(lst_gen)

# создание списка с помощью цикла и условия (фильтра):
lst_new2 = []
for el in lst_val:
    if el % 2 == 0:  # число el четное (остаток от деления на 2 равен 0)
        lst_new2.append(el * 2)
print(lst_new2)

# создание аналогичного списка при помощи генератора:
lst_gen2 = [el * 2 for el in lst_val if el % 2 == 0]
print(lst_gen2)

filt_list = [1, 3, 2, 8, 4, 11, 8, 9]
for ind in range(len(filt_list) - 1, -1, -1):  # идем с конца в начало с шагом -1
    el = filt_list[ind]
    print(f"ind: {ind}, el: {el}")
    #     do_action(element)
    if el % 2 == 0:
        print("removing")
        del filt_list[ind]
print(filt_list)  # РАБОТАЕТ!
