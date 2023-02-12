#!/usr/bin/node
/*
    prints all characters of a Star Wars movie
    with particular ID
*/
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    const characters = jsonBody.characters;
    for (const character of characters) {
      request(character, function (errorC, responseC, bodyC) {
        if (errorC) {
          console.log('code:', response.statusCode);
        }
        const characterData = JSON.parse(bodyC);
        console.log(characterData.name);
      });
    }
  }
});
