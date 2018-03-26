var generator = function() {
    var number = 0;
    return function() {
        number += 10;
        return number;
    };
};

var g = generator();
console.log(g());
console.log(g());
console.log(g());
console.log(g());
