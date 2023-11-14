#!/usr/bin/node

const dict = require('./101-data.js').dict;

const id = Object.keys(dict);
const occurence = [];
id.forEach(id => {
  if (!(dict[id] in occurence)) { occurence.push(dict[id]); }
});

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
