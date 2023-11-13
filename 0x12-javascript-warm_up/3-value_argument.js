#!/usr/bin/node

const len = function (array) {
  let size = 0;
  /* eslint-disable no-unused-vars */
  for (const element of array) {
    size++;
  }
  return size;
};

if (len(process.argv) <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
