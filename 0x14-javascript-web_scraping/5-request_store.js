#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error || !response) {
    return;
  }

  fs.writeFile(args[3], body, { encoding: 'utf8' }, err => {
    return err;
  });
});
