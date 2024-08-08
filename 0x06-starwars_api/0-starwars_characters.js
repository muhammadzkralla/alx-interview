#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const names = JSON.parse(body).characters;
  loop(names, 0);
});
const loop = (names, i) => {
  if (i === names.length) return;
  request(names[i], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    loop(names, i + 1);
  });
};