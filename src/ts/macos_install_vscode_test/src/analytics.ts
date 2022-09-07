const button: HTMLButtonElement = document.querySelector("button")!;

button.addEventListener("click", () => {
  console.log("clicked!");
  let a: number = 1;
  console.log(a);
  a += 1;
  console.log(a);
});

class Person {
  name: string;
  private bills: string[] = [];
  readonly id: string = '123';

  constructor(n: string){
    this.name = n;
  }

  introduce(this: Person) {
    console.log("My name is: ", this.name);
  } 

  addBill(billName: string) {
    this.bills.push(billName);
  }

  printBills() {
    console.log(this.bills);
  }

}

const leo = new Person('Leo');
leo.introduce();
leo.addBill('water');
leo.addBill('energy');
leo.printBills();
console.log(leo.id);
console.log(leo)