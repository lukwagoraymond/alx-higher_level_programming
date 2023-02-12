#!/usr/bin/node
/*
    Prints the Star Wars movie where the episode
    number matches a given integer
*/
const request = require('request');
const movieID = parseInt(process.argv[2]);
const urlBase = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(urlBase, function (error, response, body) {
    if (error) {
        console.log(error);
    } else {
        if (response.statusCode === 200) {
            console.log(JSON.parse(body).title);
        }
    }
});
