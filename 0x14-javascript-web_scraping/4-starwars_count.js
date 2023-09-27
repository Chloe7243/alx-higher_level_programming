#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  const data = JSON.parse(response.body);
  let episodes = 0;
  data.results.forEach((episode) => {
    if (episode.characters.filter((x) => x.includes('/people/18/')).length != 0) {
      episodes++;
    };
  });
  console.log(episodes);
});
