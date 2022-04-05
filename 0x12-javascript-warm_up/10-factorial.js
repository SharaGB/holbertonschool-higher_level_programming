#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num > 1) {
    return num * factorial(num - 1);
  }
  return 1;
}

console.log(factorial(num));
