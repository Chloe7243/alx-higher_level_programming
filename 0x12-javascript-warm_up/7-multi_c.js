#!/usr/bin/node
const argv = process.argv;
if (!argv[2]) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < Number(argv[2]); i++) {
  console.log('C is fun');
}
