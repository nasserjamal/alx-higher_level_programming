#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let s = '';
    for (let x = 0; x < this.height; x++) {
      for (let x = 0; x < this.width; x++) {
        s += 'X';
      }
      if (x < this.height - 1) {
        s += '\n';
      }
    }
    console.log(s);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
