#!/usr/bin/node

const request = require('request');

const url = process.argv[1];

request(url, function(error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log("code:", response.statusCode);
  }
});
