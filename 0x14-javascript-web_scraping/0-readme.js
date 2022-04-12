#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, (err, data) => {
  if (err) {
    return console.error((err));
  }
  console.log(data.toString('utf8'));
});
