#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${args[2]}`, (error, response, body) => {
  if (error || !response) {
    return;
  }
  const data = JSON.parse(response.body);
  console.log(data.title);
});
