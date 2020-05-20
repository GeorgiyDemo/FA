import math
class Arc(object):
    def __init__(self,x):
        if x<-1:
            self.x=x
        else:
            raise ValueError('Дебил,в моем варинте х должен быть меньше -1')

    def res_n(self,n):
        res=-(math.pi/2)
        koef=-1
        step=1
        for i in range(n):
            res+=1/(koef*(self.x)**step)
            step+=2
            if i%2==0:
                koef=-koef+2
            else:
                koef=-koef-2
        return res


    def res_e(self,e):
        res=-(math.pi/2)
        p_res=0
        koef=-1
        step=1
        i=0
        while abs(res-p_res)>=e:

            p_res=res
            res+=1/(koef*(self.x)**step)
            step+=2
            if i%2==0:
                koef=-koef+2
            else:
                koef=-koef-2
            i+=1
        return res

if __name__=='__main__':
    x=int(input())
    while True:
        try:
            solve=Arc(x)
        except ValueError as e:
            print(e)
        else:
            break
        n=int(input())
        e=float(input())
        print(f'Summ {n} member of row: {solve.res_n(n)}')
        print(f'Summ with accur epsilon={e}: {solve.res_e(e)}')
        print(f'Arctang({x})={math.atan(x)} Result with math.atan')