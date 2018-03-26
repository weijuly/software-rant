var generator = function() {
    var number = 0;
    return function() {
        number += 10;
        return number;
    };
};

var g = generator();
console.log(g()); // 10
console.log(g()); // 20
console.log(g()); // 30
console.log(g()); // 40
