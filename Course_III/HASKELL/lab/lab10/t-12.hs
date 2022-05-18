-- Вариант b

{-
Построить КА, допускающий цепочки из {0,1}* 
в них есть подцепочка 11 и подцепочка 00 

-}

-- Проверка на единицу или 0, если не 1 и не 0 -> False
isZeroOrOne :: Char -> Bool
isZeroOrOne x = x == '0' || x == '1'


isSubStringFound :: String -> String -> Bool
isSubStringFound [] _ = True
isSubStringFound _ [] = False
isSubStringFound (x:xs) (y:ys)
  | x == y = isSubStringFound xs ys
  | otherwise = isSubStringFound (x:xs) ys
  
zeroOneChain19 :: String -> Bool
zeroOneChain19 s = let

  match2 ('0':'0':xs) = find00 xs "00"
  match2 _ = False


  find00 _ [] = True
  find00 (x:xs) (p:ps)
    | x == p = find00 xs ps
    | otherwise = find00 xs "00" 
  find00 _ _ = False

  in
    match2 s && all isZeroOrOne s


main = do
    print(zeroOneChain19 "00")
    print(zeroOneChain19 "11")
    print(zeroOneChain19 "0011")
    print(zeroOneChain19 "1100")
    print(zeroOneChain19 "001100")
    print(zeroOneChain19 "110011")
    print("---")
    print(isSubStringFound "11" "122")
    print(isSubStringFound "11" "123")
    print(isSubStringFound "55" "12341556")