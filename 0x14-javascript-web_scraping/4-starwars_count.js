#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error || !response) {
    return;
  }
  const data = JSON.parse(body);
  let episodes = 0;
  data.results.forEach((episode) => {
    if (episode.characters.filter((x) => x.includes('/people/18/')).length !== 0) {
      episodes++;
    }
  });
  console.log(episodes);
});
