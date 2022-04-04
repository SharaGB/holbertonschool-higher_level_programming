#!/usr/bin/node
const x = parseInt(process.argv[2]);
let num = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (num < x) {
    console.log('C is fun');
    num++;
  }
}
