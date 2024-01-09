#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);

fs.readFile(args[0], 'utf8', (err, dataA) => {
  if (err) {
    console.error(err.message);
    process.exit(1);
  }

  fs.readFile(args[1], 'utf8', (err, dataB) => {
    if (err) {
      console.error(err.message);
      process.exit(1);
    }

    const concatenatedContent = dataA + dataB;

    fs.writeFile(args[2], concatenatedContent, (err) => {
      if (err) {
        console.error(err.message);
        process.exit(1);
      }

      console.log(`The content of ${args[0]} and ${args[1]} has been concatenated to ${args[2]}`);
    });
  });
});
