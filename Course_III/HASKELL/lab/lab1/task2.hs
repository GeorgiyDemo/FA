-- Функция isParallel, возвращающая True, если два отрезка, концы которых задаются в аргументах функции, параллельны (или лежат на одной прямой). Например, значение выражения isParallel (1,1) (2,2) (2,0) (4,2) должно быть равно True, поскольку отрезки (1,1) − (2,2) и (2,0) − (4,2) параллельны.
main :: IO ()

isParallel :: (Num a, Eq a) => (a,a) -> (a,a) -> (a,a) -> (a,a) -> Bool
isParallel (x0,y0) (x1,y1) (x2,y2) (x3,y3) = (y1-y0)*(x3-x2) == (x1-x0)*(y3-y2)

main = print (isParallel 1 1 2 2 2 0 4 2)