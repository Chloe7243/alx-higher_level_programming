#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${args[2]}`, (error, response, body) => {
  if (error || !response) {
    return;
  }
  const data = JSON.parse(body);
  data.characters.forEach((url) => {
    request(url, (error, response, body) => {
      if (error || !response) {
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
