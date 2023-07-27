#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    console.log('1');
  } else if (n <= 1) {
      console.log('1');
    } else {
        console.log(n * factorial(n - 1));
    }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
