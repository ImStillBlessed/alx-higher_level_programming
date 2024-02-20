#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./0-readme.js <file_path> <string_to_write>');
  process.exit(1);
}

const data = process.argv[3];
const filePath = process.argv[2];

fs.writeFile(filePath, data, err => {
  if (err) {
    console.error(err);
  }
});
