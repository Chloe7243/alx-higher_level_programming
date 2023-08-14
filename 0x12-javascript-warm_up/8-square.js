#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || !Number(argv[2])) {
  console.log('Missing size');
}

for (let i = 0; i < Number(argv[2]); i++) {
  console.log(''.padEnd(Number(argv[2]), 'X'));
}
