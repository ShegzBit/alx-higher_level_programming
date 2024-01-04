#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) { console.error(err); return; }
  let i = 0;
  JSON.parse(body).results.forEach(result => {
    result.characters.forEach(url => {
      if (url.endsWith('/18/')) i++;
    });
  });
  console.log(i);
});
