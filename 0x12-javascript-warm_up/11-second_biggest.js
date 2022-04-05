#!/usr/bin/node
const argc = process.argv.slice(2);

if (argc.length === 0 || argc.length === 1) {
  console.log(0);
} else {
  argc.sort();
  console.log(argc[argc.length - 2]);
}
