-- Задание 3

{-
6) Функция removeOdd, которая удаляет из заданного списка целых чисел все нечетные числа. Например:
removeOdd [1,4,5,6,10] должен возвращать [4,10].
-}

removeOdd :: [Integer] -> [Integer]
removeOdd [] = []
removeOdd (x:xs) = if odd x then removeOdd xs else x : removeOdd xs

{-
Задание по выбору. Функция countTrue :: [Bool] -> Integer, возвращающая количество элементов списка, равных True.
-}
countTrue :: [Bool] -> Integer
countTrue [] = 0
countTrue (x:xs) = if (x == True) then (1 + countTrue(xs)) else countTrue(xs)

main = do 
   print (removeOdd [1,4,5,6,10])
   print (countTrue [True, False, True])
