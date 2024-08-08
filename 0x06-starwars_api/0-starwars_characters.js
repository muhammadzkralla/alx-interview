#!/usr/bin/node

const request = require('request');

const base_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(base_url, function (error, response, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  loop(characters, 0);
});
const loop = (characters, x) => {
  if (x === characters.length) return;
  request(characters[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    loop(characters, x + 1);
  });
};