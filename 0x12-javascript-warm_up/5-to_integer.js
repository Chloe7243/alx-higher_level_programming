#!/usr/bin/node
const argv = process.argv;
console.log(!Number(argv[2]) ? 'Not a number' : `My number: ${Number(argv[2])}`);
