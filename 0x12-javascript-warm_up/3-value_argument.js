#!/usr/bin/node
const argc = process.argv;
if (argc[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argc[2]);
}
