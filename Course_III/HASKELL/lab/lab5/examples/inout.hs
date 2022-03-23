do1 s = s

rInt:: [Char]->Integer
rInt s = read s
sInt s = map rInt (words s)  -- "1 2 3" --> [1,2,3]
do2 s = show $ sInt s

-- ввод данных из файла, обработка и вывод результата
inout f0 f1 dox = do {
	s1 <- readFile f0
	; writeFile f1 (dox s1)
}

main f = inout "f0.txt" "f1.txt" f
main1 = inout "f0.txt" "f1.txt" do1
main2 = inout "f0.txt" "f1.txt" do2


f2::IO Int
f2 = do {return 2}
ff,fi :: Int -> IO Int
ff x = do {return (x*x)}
fi x = do {return x}

fdo :: IO ()
fdo = do {x <- f2;    -- 2+5+2*2
		  z <- fi 5;	
          y <- ff x; 
          putStr ("res=" ++ show (x+y+z)) 
		  }
