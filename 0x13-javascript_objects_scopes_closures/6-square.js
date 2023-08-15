#!/usr/bin/node
const MSquare = require('./5-square');
module.exports = class Square extends MSquare {
  constructor(size) {
    super(size);
  }

  charPrint(c = 'x') {
    for (let i = 0; i < this.height; i++) {
      console.log(''.padEnd(this.width, c));
    }
  }
};
