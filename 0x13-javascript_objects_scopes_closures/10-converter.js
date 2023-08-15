#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (n) {
    n.toString(base);
  }
  return myConverter;
};
