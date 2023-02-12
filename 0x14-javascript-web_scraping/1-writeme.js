#!/usr/bin/node
/*
    Writes a string to a file
*/

const fs = require('fs');
const fileName = process.argv[2];
const string = process.argv[3];

fs.writeFile(fileName, string, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
