const button: HTMLButtonElement = document.querySelector("button")!;

button.addEventListener("click", () => {
  console.log("clicked!");
  let a: number = 1;
  console.log(a);
  a += 1;
  console.log(a);
});
