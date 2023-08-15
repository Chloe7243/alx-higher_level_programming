#!/usr/bin/node
const dict = require('./101-data').dict;
const newObject = {};
for (const item of Object.values(dict)) {
  newObject[item] = Object.keys(dict).filter((key) => dict[key] === item);
}
console.log(newObject);
