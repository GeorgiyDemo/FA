{-
ПИ19-3 Деменчук Георгий

Задача t-11. Удалить из программы комментарии.
Для исходного файла проверяется расширение (если расширение не соответствует, ничего не делать)
на Паскале (расширение *.pas), комментарии (* ….. *)
Результат (программа без комментариеа) выдается в другой файл, имя которого формируется по некоторому правилу
-}

-- Библиотека нужна для чтения и записи в файл
import System.IO

-----------------------------------------Валидация разрешения файла--------------------------------
--Получение типа типа-разрешения файла
getFileType p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : getFileType p s''
                            where (w, s'') = break p s'


-- Проверка на корректный тип файла
-- Если файл .pas, то вызывает dataReader
-- Если файл не .pas, то пишет некорректнй тип файла
fileTypeValidator :: [Char] -> IO ()
fileTypeValidator file_name = if last (getFileType (=='.') file_name)  == "pas" 
                            then dataReader "file.pas" 
                            else print("Not .pas file")
--------------------------------------------------------------------------------------------

----------------------------------------------Работа с исходным файлов--------------------------------
-- Чтение данных из файла
dataReader path = do
            contents <- readFile path
            let buff = dataCommentRemover (lines contents)
            print("Comments was deleted")
            dataDumper path buff

-- Сохранение данных в файл
dataDumper path data_edited = do
    -- Запись в выходной файл
    outh <- openFile ("new_" ++ path) WriteMode
    hPutStrLn outh (filter (/='"') (foldr (\a b -> a ('\n' : b)) "\n" (map shows data_edited)))
    -- Закрытие выходного файла
    hClose outh
    print("dataDumper -> ok")
--------------------------------------------------------------------------------------------------------

-- Удаление комментария из строки   
dataCommentRemover [] = []
dataCommentRemover (l:ls) =
	if (((last l) == ')') && (head (tail l) == '*')) then dataCommentRemover ls else  l:(dataCommentRemover ls)

--------------------------------------------------------------------------------------------------------

-- Точка входа в программу
main = do
    -- Вызов функции проверки типа файла
    fileTypeValidator("file.pas")