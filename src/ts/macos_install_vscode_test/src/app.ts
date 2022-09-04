function add(n1: number, n2: number): number {
  return n1 + n2;
}

console.log("hello world...");
console.log("bye bye...");

const number1 = "3";
const number2 = 2.8;
let s1: string = "hello";
let b1: boolean = true;
let n3: number;
n3 = 123;

const result = add(+number1, number2);
console.log(result);
console.log(n3, s1, b1);

// object type
const person: {
  name: string;
  age: number;
} = {
  name: "Loe",
  age: 111,
};

console.log(person.name);

// array
const group: string[] = ["Leo", "Sam"];
const groupMix: any[] = ["abc", 1];
for (const mem of group) {
  console.log(mem);
}

// tuple
const tu: (string | number)[] = [2, "author"]; //array
const tu2: [number, string] = [2, "author"]; //tuple: fixed length, fixed type

// enum
enum Role {
  ADMIN = 1,
  READ_ONLY,
  AUTHOR,
}
console.log(Role.ADMIN);

// any type
let whatever: any;
whatever = 2;
whatever = "a";

// union type
let unionTypeVar: number | string = 3;

// literal type
let literalTypeVar: 1 | 3 = 3;

// custom type
type Custom = number | boolean;
const customTypeVar: Custom = false;

// void vs undefined
function printResult(num: Custom): void {
  console.log(num);
}

function returnUndefined(): undefined {
  return;
}

printResult(customTypeVar);

returnUndefined();

// Function
let handleFunc: (a: number, b: number) => number;
handleFunc = add;
console.log(handleFunc(2, 3));

// Callback
function addAndHandle(n1: number, n2: number, cb: (num: number) => void) {
  const result = n1 + n2;
  cb(result);
}
addAndHandle(10, 20, (result) => {
  console.log(result);
});

// unknown type
// any allows other type to assign to it, but unknown does not allow unless you check
let userInput: unknown;
let userName: string;
userInput = 5;
userInput = "Max";
if (typeof userInput === "string") {
  // need this check for unknown
  userName = userInput;
}

// never type -> for throw error
function generateError(message: string, code: number): never {
  throw { message: message, errorCode: code };
}
generateError("Hello error! ", 500);
