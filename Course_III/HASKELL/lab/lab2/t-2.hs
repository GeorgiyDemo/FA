-- Задание 2

{-Определите функцию, принимающую на вход целое число n и
возвращающую список, содержащий n элементов, упорядоченных по возрастанию.
-}

-- 6) Список степеней двойки.
powers :: Integer -> [Integer]
powers 0 = [1]
powers n = (powers (n-1)) ++ [2^n]

--4) Задание по выбору. Список факториалов
custom :: Integer -> [Integer]
factorial 0 = 1
factorial x = x * factorial(x-1)
custom 0 = [ ]
custom x = custom (x-1) ++ [factorial(x)]  

main = do 
   print (powers 10)
   print(custom 10)