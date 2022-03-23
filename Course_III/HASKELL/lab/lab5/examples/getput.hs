import IO
main = do
	c <- getChar
	putChar c

isReady :: IO Bool
isReady = do
	c1 <- getChar
--	putChar c1
	return (c1=='y')
	
getStr :: IO String
getStr = do
	c <- getChar
	if (c == '\n') 
	then return "" 
	else do 
		cs <- getStr
		return (c:cs)

getStr1 = do {c <- getChar;
	if (c == '\n')then return "" 
	else do{cs <- getStr1; return (c:cs)}}

	
--putStr1 :: [Char] -> IO ()
putStr1 s = do
	if s=="" 
	then putChar '\n'
	else do
	putChar (head s)
	putStr1 (tail s)
	
--putStr [c:s] = do putChar c; putStr s

fs = do {s <- getStr; putStr1 s}

todoList :: [IO()]  -- список действий
todoList = [putChar 'a',do {putChar 'b'; putChar 'c'},
	do {c <- getChar; putChar c}]

seq1 :: [IO ()] -> IO ()
seq1 [] = return ()
seq1 (a:as) = do {a; seq1 as}

copyfile f1 f2 = do {
     fin <- catch (openFile f1 ReadMode)  (\_ -> error "Cannot open f1" )
    ; fto <- catch (openFile f2 WriteMode) (\_ -> error "Cannot open f2" )
    ; ss  <- hGetContents fin
    ; hPutStr fto ss  
    ; hClose fto
    ; putStr "Done."
   }
   
copyf f0 f1 = do {
  ss <- readFile f0
  ; writeFile f1 ss 
}   
