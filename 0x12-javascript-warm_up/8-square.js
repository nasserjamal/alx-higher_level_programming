#!/usr/bin/node

const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  let s = '';
  for (let height = 0; height < x; height++) {
    for (let width = 0; width < x; width++) {
      s += 'X';
    }
    if (height < x - 1) {
      s += '\n';
    }
  }
  console.log(s);
}
