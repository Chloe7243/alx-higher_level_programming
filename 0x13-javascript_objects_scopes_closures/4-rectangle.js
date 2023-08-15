#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || w < 0 || h < 0 || !h) {
      const obj = {};
    }
    else {
    this.width = w;
    this.height = h;
    }
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log(''.padEnd(this.width, 'X'));
    };
  }

  rotate() {
    let height = this.height;
    this.height = this.width;
    this.width = height;
  }

  double() {
    this.height *= 2;
    this.width *= 2;
  }
};
