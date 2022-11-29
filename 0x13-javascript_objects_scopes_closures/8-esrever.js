#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  for (let indx = list.length - 1; indx >= 0; indx--) {
    newList.push(list[indx]);
  }
  return newList;
};
