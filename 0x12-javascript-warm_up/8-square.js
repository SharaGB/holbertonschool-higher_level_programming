#!/usr/bin/node
const x = parseInt(process.argv[2]);
let square = 0;
const X = 'X';

if (isNaN(x)) {
  console.log('Missing size');
} else {
  while (square < x) {
    console.log(X.repeat(x));
    square++;
  }
}
