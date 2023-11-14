#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(element => element === searchElement);
  return newList.length;
};
