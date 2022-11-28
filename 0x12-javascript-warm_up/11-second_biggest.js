#!/usr/bin/node

function getI (myList) {
  let i;
  const myListLength = myList.length;
  if (myList[myListLength - 1] === myList[myListLength - 2]) {
    let y = myListLength - 1;
    while (myList[y] === myList[y - 1]) {
      y -= 1;
      if (y - 1 === -1) {
        return -1;
      }
    }
    i = y - 1;
    return i;
  } else {
    i = myListLength - 2;
    return i;
  }
}

function secondBiggest (myList) {
  myList = myList.sort();
  const i = getI(myList);
  const myListLength = myList.length;
  const sndLastIndex = i;

  if (myListLength === 0 || myListLength === 1 || sndLastIndex === -1) {
    console.log('0');
  } else {
    console.log(myList[sndLastIndex]);
  }
}

secondBiggest(process.argv.slice(2));
