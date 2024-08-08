#!/usr/bin/node

const request = require('request');

const base_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(base_url, function (error, response, body) {
  if (error) throw error;
  const characters = JSON.parse(body).characters;
  loop(characters, 0);
});
const loop = (characters, i) => {
  if (i === characters.length) return;
  request(characters[i], function (err, res, bd) {
    if (err) throw err;
    console.log(JSON.parse(bd).name);
    loop(characters, i + 1);
  });
};