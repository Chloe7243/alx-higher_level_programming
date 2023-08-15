#!/usr/bin/node
const MSquare = require('./5-square');
module.exports = class Square extends MSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
