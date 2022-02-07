/*
10)	Свертка. Используйте метод reduce в комбинации с
concat для свёртки массива массивов в один массив,
у которого есть все элементы входных массивов.
 */
let arr = [
    ["Cat"],
    [1, 2, 3],
    [5, 5],
    [6, 7],
    ["cat"]
];

arr = arr.reduce((a, b) => {
    console.log(b)
    return a.concat(b);
});
console.log(arr);
 
 