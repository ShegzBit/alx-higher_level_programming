#!/usr/bin/node
const fs = require('fs');

// get file name and open file for reading
const filename = process.argv[2];

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    // print file to screen
  } else {
    console.log(data);
  }
});
