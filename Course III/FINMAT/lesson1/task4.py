# F - номинал облигации
# C - купонная выплата
# P0 - приведенная внутренняя цена облигации
# n - число купонных доходов
F = 100
c = 0.07
n = 4

i0 = 0.1


r = 0.06
C = c * F

p_koeffs = []

for t in range(1,n+1):
    koeff = C/((1+i0)**t)
    print(f"Коэфф при t={t}: {koeff}")
    p_koeffs.append(koeff)

P0 = sum(p_koeffs) + F/((1+i0)**n)
print(f"Полученное P0: {P0}")



duration_koeffs = []
for t in range(1,n+1):
    koeff = t *C/((1+i0)**t)
    print(f"Коэфф при t={t}: {koeff}")
    duration_koeffs.append(koeff)

D = (1/P0) * (sum(duration_koeffs) + n* (F/((1+i0)**n)))

print(f"Полученная дюрация: {D}")

D_modify = D/(1+i0)
print(f"Полученная мод дюрация: {D_modify}")

delta_P = -D_modify*P0*r

print(f"Изменение цены: {delta_P}")
