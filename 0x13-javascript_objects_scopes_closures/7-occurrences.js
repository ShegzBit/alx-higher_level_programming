#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let newList = list.filter(element => element == searchElement);
  return newList.length;
}