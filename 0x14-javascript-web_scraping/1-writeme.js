#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

fs.writeFile(args[2], args[3], { encoding: 'utf8' }, err => {
  if (err) {
    console.error(err);
  }
});
