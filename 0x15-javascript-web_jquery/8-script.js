/*
    fetches and lists all movie titles by using this URL
*/
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, textStatus) {
    data.results.map((movie) => $('UL#list_movies').append('<li>' + movie.title + '</li>'));
});