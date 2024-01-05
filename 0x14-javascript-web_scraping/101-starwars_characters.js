#!/usr/bin/node

const request = require('request');
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
const util = require('util');

function getWrapper (url, callback) {
  if (!url) { return; }
  request.get(url, (err, res, body) => {
    if (err) { callback(err, null); return; }
    callback(null, body);
  });
}

const promGet = util.promisify(getWrapper);
function recurPrint (characters, promise) {
  if (characters.length >= 0) {
    promise.then((body) => {
      console.log(JSON.parse(body).name);
      recurPrint(characters, promGet(characters.shift()));
    }).catch((err) => console.log(err));
  }
}
request.get(filmUrl, (err, res, body) => {
  if (err) { console.error(err); return; }
  const characters = Array.from(JSON.parse(body).characters);
  recurPrint(characters, promGet(characters.shift()));
});
