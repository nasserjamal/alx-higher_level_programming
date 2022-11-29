#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const elmnt of list) {
    if (elmnt === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
