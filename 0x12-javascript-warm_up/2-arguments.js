#!/usr/bin/node
// Include process module
const process = require('process');
const argc = process.argv.length - 1;
if (argc === 1) {
  console.log('No argument');
} else if (argc === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
