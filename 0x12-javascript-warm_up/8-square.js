#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || !Number(argv[2])) {
  console.log('Missing size');
}

for (let i = 0; i < Number(argv[2]); i++) {
  const line = [];
  for (let j = 0; j < Number(argv[2]); j++) {
    line.push('X');
  }
  console.log(line.join(''));
}
