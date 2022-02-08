/*
9)	Глубокое сравнение. Оператор == сравнивает переменные объектов, проверяя,
ссылаются ли они на один объект.
Но иногда полезно было бы сравнить объекты по содержимому.
Напишите функцию deepEqual, которая принимает два значения и возвращает true,
только если это два одинаковых значения или это объекты, свойства которых имеют
одинаковые значения, если их сравнивать рекурсивным вызовом deepEqual.

Чтобы узнать, когда сравнивать величины через ===, а когда – объекты по содержимому,
используйте оператор typeof.
Если он выдаёт “object” для обеих величин,
значит нужно делать глубокое сравнение.
Не забудьте об одном дурацком исключении,
случившемся из-за исторических причин: “typeof null” тоже возвращает “object”
 */

function deepEqual(a, b) {
    if (a === b) {
        return true;
    }

    if (a == null || typeof (a) != "object" ||
        b == null || typeof (b) != "object") {
        return false;
    }

    for (const i in a) {
        if (!(i in b) || !deepEqual(a[i], b[i])) {
            return false;
        }
    }
    return true;
}


const obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
console.log(deepEqual(obj, {here: 1, object: 2}));
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
