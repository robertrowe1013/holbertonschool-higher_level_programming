#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (i) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  });
});
