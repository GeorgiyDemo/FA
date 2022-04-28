{-
Вариант 18
Построить из списков (a1,a2,..) и (b1,b2,..) список (a1,0,b1,a2,0,b2,...) 
-}

-- Конкатинация двух списков
merge :: [a] -> [a] -> [a]
merge xs     []     = xs
merge []     ys     = ys
merge (x:xs) (y:ys) = x : y : merge xs ys

-- Добавляет указанное число в список после каждого N элемента
insert :: Int -> a -> [a] -> [a]
insert n y xs = countdown n xs where
   countdown 0 xs = y:countdown n xs
   countdown _ [] = []
   countdown m (x:xs) = x:countdown (m-1) xs

-- Точка входа в приложение
main :: IO ()
main = do

    let list1 = [1, 2, 3, 4, 5]
    let list2 = [10, 11, 12]
    print(list1)
    print(list2)
    print(insert 1 0 (merge list1 list2))