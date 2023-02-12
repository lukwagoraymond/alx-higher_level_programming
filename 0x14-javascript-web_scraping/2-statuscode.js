#!/usr/bin/node
/*
    Displays the status code of a GET method
*/
const request = require('request');
const urlBase = process.argv[2];

request(urlBase, function (error, response) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    console.log('code:', response.statusCode);
  }
});
