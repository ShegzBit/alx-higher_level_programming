#!/usr/bin/node

const fs = require('fs');

const source1 = process.argv[2];
const source2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(source1, (err, data) => {
  if (err) throw err;
  fs.appendFile(dest, data, (err) => { if (err) throw err; });
});

fs.readFile(source2, (err, data) => {
  if (err) throw err;
  fs.appendFile(dest, data, (err) => { if (err) throw err; });
});
