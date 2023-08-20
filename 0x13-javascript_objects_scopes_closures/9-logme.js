#!/usr/bin/node
const args = [];
exports.logMe = function (item) {
  console.log(`${args.length}: ${item}`);
  args.push(item);
};
