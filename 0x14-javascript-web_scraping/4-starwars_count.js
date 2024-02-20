#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  const character = JSON.parse(body);
  console.log((character.films).length)
})

