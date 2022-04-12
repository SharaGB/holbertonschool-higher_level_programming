#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request({ url: url, json: true }, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const numTask = {};
    for (const API of body) {
      if (API.completed === true) {
        if (numTask[API.userId] === undefined) {
          numTask[API.userId] = 0;
        }
        numTask[API.userId] += 1;
      }
    }
    console.log(numTask);
  }
});
