#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const data = process.argv[3];

fs.writeFileSync(filename, data);
