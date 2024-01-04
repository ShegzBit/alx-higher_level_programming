#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) { console.error(err); return; }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) { console.error(err); }
  });
});
