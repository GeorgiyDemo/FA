{-
ПИ19-3 Деменчук Георгий
Вариант 16
Переставить местами максимальный и минимальный элементы списка
-}

-- Максимальный индекс и элемент в списке
maxim :: (Ord a) => [a] -> (a, Int)
maxim l = 
  let pmaxim :: (Ord a) => [a] -> Int -> (a, Int)
      pmaxim [] _  = error "Пустой список"        -- Если список пустой, выдаем ошибку
      pmaxim [x] xi = (x, xi)                     -- В списке есть один элемент, возвращаем его и его индекс
      pmaxim (x:xs) xi                            -- Более одного элемента, разбиваем список на части
        | x > t     = (x, xi)                     -- Если текущий элемент больше, возвращаем его и его индекс
        | otherwise = (t, ti)                     -- Если в конце списка есть элемент большего размера, возвращаем его
        where (t, ti) = pmaxim xs (xi + 1)        -- Получаем максимум из конца списка
  in pmaxim l 0                                   -- Вызов внутренней функции с начальным индексом

-- Получение максимального индекса
maxIndex :: (Ord a) => [a] -> Int
maxIndex l = snd (maxim l)

-- Минимальный индекс и элемент в списке
minim :: (Ord a) => [a] -> (a, Int)
minim l = 
  let pminim :: (Ord a) => [a] -> Int -> (a, Int) 
      pminim [] _  = error "Пустой список"        -- Если список пустой, выдаем ошибку
      pminim [x] xi = (x, xi)                     -- В списке есть один элемент, возвращаем его и его индекс
      pminim (x:xs) xi                            -- Более одного элемента, разбиваем список на части
        | x < t     = (x, xi)                     -- Если текущий элемент меньше, возвращаем его и его индекс
        | otherwise = (t, ti)                     -- Если в конце списка есть элемент меньшего размера, возвращаем его
        where (t, ti) = pminim xs (xi + 1)        -- Получаем максимум из конца списка
  in pminim l 0                                   -- Вызов внутренней функции с начальным индексом

-- Получение минимального индекса
minIndex :: (Ord a) => [a] -> Int
minIndex l = snd (minim l)

-- Перестановка местами элементов с указанными индексами
swapTwo :: Int -> Int -> [a] -> [a]
swapTwo f s xs = map snd . foldr (\x a -> 
        if fst x == f then ys !! s : a
        else if fst x == s then ys !! f : a
        else x : a) [] $ ys
    where ys = zip [0..] xs

-- Точка входа в приложение
main :: IO ()
main = do

    let list = [1,2,3,4,5,6,7,8,9,10]
    print(list)
    print(swapTwo (maxIndex list) (minIndex list) list)

    print("------------------------------")
    let list = [1,2,3,10,5,6,7,8,9,4]
    print(list)
    print(swapTwo (maxIndex list) (minIndex list) list)
