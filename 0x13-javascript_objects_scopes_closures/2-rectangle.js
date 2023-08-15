#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!w || w < 0 || h < 0 || !h) {
      const obj = {};
      return obj;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
