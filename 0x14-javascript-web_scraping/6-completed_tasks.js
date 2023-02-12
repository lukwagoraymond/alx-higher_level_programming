#!/usr/bin/node
/*
    Gets the contents of a webpage and
    stores them in a file
*/
const request = require('request');
const urlBase = process.argv[2];

request(urlBase, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const dictCompletedUser = {};
    for (const todo of jsonBody) {
      if (todo.completed) {
        if (dictCompletedUser[todo.userId]) {
          dictCompletedUser[todo.userId] += 1;
        } else {
          dictCompletedUser[todo.userId] = 1;
        }
      }
    }
    console.log(dictCompletedUser);
  }
});
