#!/usr/bin/node

function add (a, b) {
    // a = process.argv[2];
    // b = process.argv[3];
  
    console.log(a + b);
}
  
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
