#!/usr/bin/node

const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
  if (error || !response) {
    return;
  }
  const data = JSON.parse(response.body);
  const users = {};
  data.forEach((task) => {
    if (task.completed) {
      users[task.userId] = (users[task.userId] ?? 1) + 1;
    }
  });
  console.log(users);
});
