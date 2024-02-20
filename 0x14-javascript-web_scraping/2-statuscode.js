#!/usr/bin/node

const request = require('request');

const url = process.argv[1];

request(url, (error, response) => {
  console.error(error);
  console.log('code:', response.statusCode); 
});