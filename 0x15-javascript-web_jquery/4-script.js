#!/usr/bin/node
$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('HEADER').toggleClass('red');
    $('HEADER').toggleClass('green');
  });
});
