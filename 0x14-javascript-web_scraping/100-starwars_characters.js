#!/usr/bin/node

const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(filmUrl, (err, res, body) => {
  if (err) { console.error(err); return; }
  JSON.parse(body).characters.forEach(actor => {
    request.get(actor, (err, res, body) => {
      if (err) { console.error(err); return; }
      console.log(JSON.parse(body).name);
    });
  });
});
