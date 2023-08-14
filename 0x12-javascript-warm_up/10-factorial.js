#!/usr/bin/node
const argv = process.argv;

function factorial (a) {
  return !a ? 1 : a * factorial(a - 1);
}
console.log(factorial(Number(argv[2])));
