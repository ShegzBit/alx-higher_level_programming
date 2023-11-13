#!/usr/bin/node

const add = (a, b) => a + b;

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (process.argv.length <= 3) { console.log('NaN'); } else { console.log(add(num1, num2)); }
