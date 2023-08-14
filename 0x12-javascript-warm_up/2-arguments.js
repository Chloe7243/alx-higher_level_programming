#!/usr/bin/node
const argv = process.argv;
let msg = 'No argument';
if (argv.length > 2) {
  msg = argv.length === 3 ? 'Argument found' : 'Arguments found';
}
console.log(msg);
