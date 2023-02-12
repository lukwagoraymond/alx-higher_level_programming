#!/usr/bin/node
/*
    Prints number of movies where character
    "Wedge Antilles- ID 18" is present
*/

const request = require('request');
const urlBase = process.argv[2];

request(urlBase, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    let count = 0;
    for (const film of jsonBody.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) { // ...people/18 is Wedge Antilles
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
