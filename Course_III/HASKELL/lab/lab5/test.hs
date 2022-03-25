main = do
  action <- cmdParser
  case action of
    Add -> do username <- promptUsername
              let entry = Entry username "somepassword"
              persist entry
persist entry

promptUsername :: IO String
promptUsername = do
  putStrLn "Username to add to the password manager:"
  getLine

-- fake definitions to make things compile

persist :: Entry ->  IO ()
persist = print

cmdParser :: IO Add
cmdParser = fmap (const Add) getLine

data Add = Add deriving Show
data Entry = Entry String String deriving Show