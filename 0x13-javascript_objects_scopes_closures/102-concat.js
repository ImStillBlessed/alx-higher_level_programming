#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  process.exit(1);
}

const [, , fileA, fileB, fileC] = process.argv;

// Read the content of fileA
fs.readFile(fileA, 'utf8', (errA, dataA) => {
  if (errA) {
    console.error(errA.message);
    process.exit(1);
  }

  // Read the content of fileB
  fs.readFile(fileB, 'utf8', (errB, dataB) => {
    if (errB) {
      console.error(errB.message);
      process.exit(1);
    }

    // Concatenate the content of fileA and fileB
    const concatenatedContent = dataA + dataB;

    // Write the concatenated content to fileC
    fs.writeFile(fileC, concatenatedContent, (errC) => {
      if (errC) {
        console.error(errC.message);
        process.exit(1);
      }
    });
  });
});
