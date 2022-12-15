#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  const content = data; console.log(content); if (err !== null) {
    console.log(err);
  }
});
