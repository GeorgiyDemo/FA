factorial :: Integer -> Integer
factorial n = if n == 0 then 1 else n * factorial (n - 1)
main = do 
   putStrLn "The factorial of 10 is:"  
   print (factorial 10)