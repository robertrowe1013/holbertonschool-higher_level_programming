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
    let taskId;
    const json = JSON.parse(body);
    const newDict = {};
    for (taskId = 1; taskId < json.length; taskId++) {
      if (json[taskId].completed === true) {
        if (newDict[json[taskId].userId]) {
          newDict[json[taskId].userId] += 1;
        } else {
          newDict[json[taskId].userId] = 1;
        }
      }
    }
    console.log(newDict);
  }
});
