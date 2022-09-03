function add(n1, n2) {
    return n1 + n2;
}
console.log("hello world...");
console.log("bye bye...");
var number1 = "3";
var number2 = 2.8;
var s1 = "hello";
var b1 = true;
var n3;
n3 = 123;
var result = add(+number1, number2);
console.log(result);
console.log(n3, s1, b1);
// object type
var person = {
    name: "Loe",
    age: 111
};
console.log(person.name);
// array
var group = ["Leo", "Sam"];
var groupMix = ["abc", 1];
for (var _i = 0, group_1 = group; _i < group_1.length; _i++) {
    var mem = group_1[_i];
    console.log(mem);
}
// tuple
var tu = [2, "author"]; //array
var tu2 = [2, "author"]; //tuple: fixed length, fixed type
// enum
var Role;
(function (Role) {
    Role[Role["ADMIN"] = 1] = "ADMIN";
    Role[Role["READ_ONLY"] = 2] = "READ_ONLY";
    Role[Role["AUTHOR"] = 3] = "AUTHOR";
})(Role || (Role = {}));
console.log(Role.ADMIN);
// any type
var whatever;
whatever = 2;
whatever = "a";
// union type
var unionTypeVar = 3;
// literal type
var literalTypeVar = 3;
var customTypeVar = false;
// void vs undefined
function printResult(num) {
    console.log(num);
}
function returnUndefined() {
    return;
}
printResult(customTypeVar);
returnUndefined();
// Function
var handleFunc;
handleFunc = add;
console.log(handleFunc(2, 3));
// Callback
