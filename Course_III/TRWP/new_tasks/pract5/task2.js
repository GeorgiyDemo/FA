/*
2)	FizzBuzz. Напишите программу, которая выводит через console.log все числа от 1 до 100,
с двумя исключениями.
Для чисел, нацело делящихся на 3, она должна выводить ‘Fizz’,
а для чисел, делящихся на 5 (но не на 3) – ‘Buzz’,
Когда сумеете – исправьте её так, чтобы она выводила «FizzBuzz» для всех чисел, которые делятся и на 3 и на 5.
 */

let maxCount = 100;

for (let i = 1; i < maxCount; i++) {
    if (i % 3 === 0) {
        console.log(i, 'Fizz');
    } else if (i % 5 === 0) {
        console.log(i, "Buzz");
    } else {
        console.log(i)
    }
}

console.log("-----")
for (let i = 1; i < maxCount; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log(i, "FizzBuzz");
    } else {
        console.log(i);
    }
}

