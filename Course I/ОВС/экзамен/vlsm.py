# Калькулятор подсетей от https://github.com/noecl1/
# Переведен на Русский https://github.com/GeorgiyDemo/
# Нужен для экзамена, после экза - удалю

import os
from netaddr import *
from prettytable import PrettyTable
from colorama import init, Fore, Style, Back
import pprint

def clearTerminal():
    if os.name == 'nt':
        os.system('cls')
        pass
    else:
        os.system('clear')
        pass
    pass

def validateIP(ip):
    return ip.valid_ipv4(ip)

def printHeader():
    print('\n\n')
    print(Style.BRIGHT,Fore.WHITE,Back.BLUE)
    print("                                                ")
    print("         | | | |  Калькулятор VLSM | | | |      ")
    print("             от Noé Camacho Lizárraga           ")
    print("  https://github.com/noecl1/vlsmCalculator_ipv4 ")
    print("           Перевод на Руccкий от Демы           ")
    print("                                               ", Style.RESET_ALL, '\n\n')

def printTable(table, majorNet, neededHosts, allocatedHosts):
    clearTerminal()
    ipTemp = IPNetwork(majorNet)
    print('\n\n')
    print(Style.BRIGHT,Fore.WHITE,Back.GREEN)
    print("                                                ")
    print("         | | | |  Сеть существует  | | | |      ")
    print("                                               ", Style.RESET_ALL, '\n\n')
    print(Back.WHITE, Fore.BLACK,Style.NORMAL,Style.NORMAL,'Сеть:', Fore.WHITE, Back.GREEN, Style.BRIGHT,'{}'.format(ipTemp),Style.RESET_ALL)
    print(Back.WHITE, Fore.BLACK,Style.NORMAL,' Доступные сети в основной сети:',Fore.WHITE,Back.GREEN,Style.BRIGHT,'{}'.format(ipTemp.size),Style.RESET_ALL)
    print(Back.WHITE, Fore.BLACK,Style.NORMAL,' Кол-во IP-адресов:',Fore.WHITE, Back.GREEN,Style.BRIGHT,'{}'.format(neededHosts),Style.RESET_ALL)
    print(Back.WHITE, Fore.BLACK,Style.NORMAL,' IP-адреса в подсетях:',Fore.WHITE,Back.GREEN,Style.BRIGHT,'{}'.format(allocatedHosts),Style.RESET_ALL)
    print("\n")
    print(table)

def requestNets(netSize):

    buf_list = []
    hostSize = {}

    for i in range(netSize):
        buf_list.append(int(input('Введите кол-во хостов в подсети №'+str(i+1)+' -> '))+2)
    buf_list.sort(reverse=True)

    for hosts in range(netSize):
        hostSize[hosts+1] = buf_list[hosts]

    return hostSize

def calculateNetwork(ip, hostSize, pos):
    cidr = calculateCidr(hostSize, pos)
    temp = ip
    temp2 = temp.__str__()
    temp3 = temp2.split('/')
    del(temp3[1]) 
    temp3.append(str(cidr))
    chara= '/'
    ip = IPNetwork(chara.join(temp3))
    return ip 

def calculateCidr(hostSize, pos):
    for num in range(0,100):
        if (hostSize[pos] <= 2**num):
            return 32-num
        else:
            pass

def main():
    init()
    clearTerminal()
    printHeader()
    table = PrettyTable()
    table.field_names = ['Подсеть','Требуемый размер','Выделенно адресов','Сетевой адрес', 'Диапазон IP', 'Широковещание', 'CIDR', 'Маска']
    neededHosts = 0
    allocatedHosts = 0
    try:
        majorNet = input('Основная сеть с маской (пример: 192.168.16.0/24) -> ')
        ip = IPNetwork(majorNet)
        netSize = int(input('Кол-во подсетей -> '))
        netDict= requestNets(netSize)
        for pos in range(0, netSize):
            ip = calculateNetwork(ip, netDict, pos+1)
            ip_list = list(ip)
            table.add_row([pos+1, netDict[pos+1]-2, ip.size-2, ip.ip, '{} - {}'.format(ip_list[1], ip[len(ip_list)-2]), ip.broadcast, '/{}'.format(ip.prefixlen), ip.netmask])
            neededHosts = neededHosts + (netDict[pos+1]-2)
            allocatedHosts = allocatedHosts + (ip.size-2)
            ip = ip.next(1)
        printTable(table,majorNet, neededHosts, allocatedHosts)
    except:
        print('\n\n',Fore.WHITE, Back.RED)
        print("                                                ")
        print("         | | | |  Произошла ошибка | | | |      ")
        print("                                               ", Style.RESET_ALL, '\n\n')
    
if __name__ == "__main__":
       main()