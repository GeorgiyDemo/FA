{-
Вариант 18
Определите следующие функции с использованием функций высшего порядка:
- Переставить в матрице две строки.
-}

-- Метод для перемещения элементов списка по индексам
-- Был реализован в задании t-10
swapTwo :: Int -> Int -> [a] -> [a]
swapTwo f s xs = map snd . foldr (\x a -> 
        if fst x == f then ys !! s : a
        else if fst x == s then ys !! f : a
        else x : a) [] $ ys
    where ys = zip [0..] xs

-- Точка входа в приложение
main :: IO ()
main = do

    let textMatrix1 = [[1,2,3], [4,5,6], [7,8,9]]
    print("Matrix: " ++ show(textMatrix1))
    print("swapTwo 0 2: " ++ show(swapTwo 0 2 textMatrix1))
    print("swapTwo 0 1: " ++ show(swapTwo 0 1 textMatrix1))