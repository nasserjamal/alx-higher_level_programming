#!/usr/bin/node

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  n = n * factorial(n - 1);
  return n;
}

console.log(factorial(parseInt(process.argv[2])));
