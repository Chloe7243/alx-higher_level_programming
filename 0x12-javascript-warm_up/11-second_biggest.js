#!/usr/bin/node
const argv = process.argv;

console.log(argv.slice(2).sort((a, b) => b - a)[1] || 0);
