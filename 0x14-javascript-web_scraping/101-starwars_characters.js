#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request({ url: url, json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  const characters = body.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (err, res, body) => {
      if (err) {
        return console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
