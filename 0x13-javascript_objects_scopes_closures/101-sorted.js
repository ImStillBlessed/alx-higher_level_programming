#!/usr/bin/node

const { dict } = require('./101-data');

const newDict = {};

for (const kValue in dict) {
  const vKey = dict[kValue];

  if (!(vKey in newDict)) {
    newDict[vKey] = [];
  }
  newDict[vKey].push(kValue);
}
console.log(newDict);
