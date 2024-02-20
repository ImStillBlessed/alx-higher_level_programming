#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 2) {
  console.error('Usage: node 0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[1];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
