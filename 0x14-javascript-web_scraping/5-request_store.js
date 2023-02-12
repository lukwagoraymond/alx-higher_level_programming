#!/usr/bin/node
/*
    Gets the contents of a webpage and
    stores them in a file
*/

const request = require('request');
const fs = require('fs');
const urlBase = process.argv[2];
const fileName = process.argv[3];

request(urlBase, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fileName, body, 'utf8', (error) => {
        if (error) {
            console.log(error);
        }
    });
  }
});
