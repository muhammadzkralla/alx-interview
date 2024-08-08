#!/usr/bin/node

const request = require('request');

const base_url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(base_url, function (error, response, body)  {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (err, res, bd)  {
        if (err) throw err;
        console.log(JSON.parse(bd).name);
      });
    }
});