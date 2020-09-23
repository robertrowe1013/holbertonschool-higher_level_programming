#!/usr/bin/node
const request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    let i;
    let j;
    const json = JSON.parse(body);
    for (i = 0; i < json.results.length; i++) {
      for (j = 0; j < json.results[i].characters.length; j++) {
        if (json.results[i].characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
