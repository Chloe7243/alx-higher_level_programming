#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error || !response) {
    return;
  }

  const data = response.body;
  fs.writeFile(args[3], data, { encoding: 'utf8' }, err => {
    return err;
  });
});
