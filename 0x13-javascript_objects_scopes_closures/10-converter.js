#!/usr/bin/node
exports.converter = function (base) {
  const myConverter = (n) => n.toString(base);
  return myConverter;
};
