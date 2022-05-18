-- Вариант 6
{-
Построить КА, допускающий цепочки из {0,1}* 
в них есть подцепочка 11 и подцепочка 00 
-}

-- Проверка на единицу или 0, если не 1 и не 0 -> False
isZeroOrOne :: Char -> Bool
isZeroOrOne x = x == '0' || x == '1'


myChain :: String -> Bool
myChain s = let
  check m = let
      check' [] _ = True
      check' (y:ys) (x:xs)
        | x == y = check' ys xs
        | otherwise = check' m xs
      check' _ [] = False
    in check' m
   
  in
    -- Проверка на наличие подцепочки 11 и 00 и что элементы 0 и 1 в цепочке
    check "11" s && check "00" s && all isZeroOrOne s  

main = do
    print(myChain "00")
    print(myChain "11")
    print(myChain "0011")
    print(myChain "1100")
    print(myChain "001100")
    print(myChain "110011")
    print(myChain "1210011")