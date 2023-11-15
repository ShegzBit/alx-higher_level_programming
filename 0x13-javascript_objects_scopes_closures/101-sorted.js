#!/usr/bin/node

const dict = require('./101-data.js').dict;

const id = Object.keys(dict);
const occurence = new Set(Object.values(dict));

function createDict (keyList, values) {
  const newDict = {};
  keyList.forEach(key => { newDict[key] = []; });
  values.forEach(key => {
    const newDictKey = dict[key];
    newDict[newDictKey].push(key);
  });

  return newDict;
}
console.log(createDict(occurence, id));
