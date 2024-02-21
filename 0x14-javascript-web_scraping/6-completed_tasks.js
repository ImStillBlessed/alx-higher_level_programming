#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

const todo_dict = {}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const data = JSON.parse(body);

    let movieCount = 0;

    data.results.forEach(film => {
      if (film.characters.includes(`${apiUrl}${characterId}/`)) {
        movieCount++;
      }
    });
    console.log(movieCount);
  }
});
