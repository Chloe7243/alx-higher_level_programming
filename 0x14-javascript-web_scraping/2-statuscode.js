#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error || !response) {
    return;
  }
  console.log('code:', response && response.statusCode);
});
