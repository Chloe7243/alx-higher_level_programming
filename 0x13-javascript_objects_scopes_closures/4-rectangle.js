#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w && w >= 0 && h && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(''.padEnd(this.width, c));
    }
  }

  rotate () {
    const height = this.height;
    this.height = this.width;
    this.width = height;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
