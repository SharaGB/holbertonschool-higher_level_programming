#!/usr/bin/node
const argc = process.argv.slice(2);

if (argc.length < 2) {
  console.log(0);
} else {
  argc.sort(function(a, b){
      return a - b
  });
  console.log(argc[argc.length - 2]);
}
