#!/usr/bin/node
const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body).characters;
    json.forEach(element => {
      const opts = {
        url: element,
        method: 'GET'
      };
      request(opts, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
