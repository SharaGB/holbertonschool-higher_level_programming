#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

const fs = require('fs');
const filePath = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
