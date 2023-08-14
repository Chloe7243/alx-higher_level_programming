#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  console.log(a + b);
}
add(Number(argv[2]), Number(argv[3]));
