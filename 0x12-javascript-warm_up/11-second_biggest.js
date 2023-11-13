#!/usr/bin/node

const args = process.argv.slice(2).map(n => Number(n));
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => a - b);
  const secondBiggest = sortedArgs[args.length - 2];
  console.log(secondBiggest);
}
