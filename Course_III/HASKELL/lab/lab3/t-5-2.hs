data Area = Union [Area] | 
           Inters [Area] | 
           Empty         | 
           Rectangle Int Int Int Int |
           Circle Int Int Int deriving (Eq,Show)
 
-- Вспомогательная функция, возвращающая
-- пересечение двух отрезков в виде списка [a,b]
-- Если отрезки не пересекаются - возвращает пустой список
 
int2 :: [Int] -> [Int] -> [Int]
int2 [x11,x12] [x21,x22] | (x21 < x11) = int2 [x21,x22] [x11,x12]
int2 [x11,x12] [x21,x22] | (x12 < x21)  = []
                         | (x21 >= x11) && (x21 <= x12) && (x22 >= x11) && (x22 <= x12) = [x21,x22]
                         | otherwise = [x21,x12]
  
-- Набросок (не окончен) - пересечение двух областей
-- не хватает пересечения окружности и прямоугольника
-- и полной реализации пересечения объединений и пересечений
 
intersect :: Area -> Area -> Area
intersect Empty _ = Empty
intersect _ Empty = Empty
intersect (Rectangle x11 y11 x12 y12)
          (Rectangle x21 y21 x22 y22) = if (xx==[]) || (yy==[]) then 
                                           Empty 
                                        else 
                                           (Rectangle (xx!!0) (yy!!0) (xx!!1) (yy!!1))
         where xx = int2 [x11,x12] [x21,x22]
               yy = int2 [y12,y11] [y22,y21]
intersect (Circle x1 y1 r1)
          (Circle x2 y2 r2) = if (x1-x2)^2+(y1-y2)^2 <= (r1+r2)^2 then
                                 Inters [(Circle x1 y1 r1),(Circle x2 y2 r2)]
                              else
                                 Empty                              
intersect (Union ars) (Rectangle x1 y1 x2 y2) = (Union (map (\ a -> intersect a (Rectangle x1 y1 x2 y2)) ars))             
-- и т.п.          
                           
isEmpty :: Area -> Bool
isEmpty Empty               = True
isEmpty (Circle _ _ _)      = False
isEmpty (Rectangle _ _ _ _) = False
isEmpty (Union ars)         = all (/= Empty) ars
isEmpty (Inters ars)        = (foldl (\ acc fi -> intersect acc fi) (head ars) (tail ars))==Empty           
 
 
isRectangular :: Area -> Bool
isRectangular Empty  = False
isRectangular (Rectangle _ _ _ _) = True
isRectangular (Circle _ _ _)      = False
isRectangular (Union ars)         = all (isRectangular) ars
isRectangular (Inters ars)        = all (isRectangular) ars