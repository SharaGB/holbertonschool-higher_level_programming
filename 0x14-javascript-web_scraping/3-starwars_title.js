#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
