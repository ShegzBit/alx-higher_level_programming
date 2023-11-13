#!/usr/bin/node

const args = process.argv.slice(2).map(n => Number(n));
if (args.length <= 1) {
  console.log(0);
  process.exit(1);
}
let biggest = 0;
let result = 0;
for (const arg of args) {
  if (arg > biggest) {
    result = biggest;
    biggest = arg;
  }
}
console.log(result);
