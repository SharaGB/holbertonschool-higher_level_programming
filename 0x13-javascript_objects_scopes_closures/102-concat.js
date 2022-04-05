#!/usr/bin/node
const fs = require('fs');

const file1 = fs.readFileSync(process.argv[2]);
const file2 = fs.readFileSync(process.argv[3]);
const file3 = process.argv[4];

fs.writeFileSync(file3, file1 + file2);
