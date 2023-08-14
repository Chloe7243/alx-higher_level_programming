#!/usr/bin/node
const argv = process.argv;

function factorial (a) {
  if (!a) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(Number(argv[2])));
