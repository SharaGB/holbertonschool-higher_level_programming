#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterID = '18/';

request({ url: url, json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = body.results;
    let count = 0;
    for (const res of results) {
      for (const char of res.characters) {
        if (char.endsWith(characterID)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
