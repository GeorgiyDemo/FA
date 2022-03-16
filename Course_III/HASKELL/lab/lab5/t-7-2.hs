{-
ПИ19-3 Деменчук
Задание 8.2 (по выбору)

8.	Иерархия должностей в некоторой организации образует древовидную структуру.
Каждый работник, однозначно характеризующийся уникальным именем, имеет несколько подчиненных.
Определите тип данных, представляющий такую иерархию и опишите следующие функции:

2)	getAllSubordinate, возвращающую список всех подчиненных данного работника, включая косвенных.
-}

-- Создаем кастомный тип, согласно заданию
-- у каждого работника есть массив подчиненных
data Employee = JobWorker (String) [Employee] deriving (Show, Eq)

-- Метод по поиску значения
find ((employee, emp) :xs) manager =
    if employee == manager then emp
    else find xs manager

-- Список имён работников
workerNamesList (JobWorker (n) emp) = n:concatMap workerNamesList emp

-- Список всех работников
employeeList (JobWorker (name) emp) = (name, emp):concatMap employeeList emp

-- getAllSubordinate, возвращает список всех подчиненных  работника
getAllSubordinate employee (JobWorker (name) emp) = 
    concat (map (\item -> workerNamesList item) (find (employeeList
    (JobWorker (name) emp)) employee))

-- Точка входа в приложение
main = do

    -- Формируем тестовую иерархию работников 1
    print(getAllSubordinate "Ivanov" (
        JobWorker "Ivanov"[
            JobWorker "Petrov"
                [
                    JobWorker "Sidorov" [],
                    JobWorker "Demko" [],
                    JobWorker "Dmitriev" []
                ],
            JobWorker "Maximov" []
        ]
        ))

    -- Представляем иерархию работников в виде чисел для наглядности
    print(getAllSubordinate "Petrov" (
        JobWorker "Petrov" [JobWorker "1"
                            [JobWorker "1.1" [],
                            JobWorker "1.2" [],
                            JobWorker "1.3" []
                            ],
                        JobWorker "2"
                            [JobWorker "2.1" [
                                JobWorker "2.1.1" []
                            ],
                            JobWorker "2.2" [],
                            JobWorker "2.3" []
                            ]
                        ]))