#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[4], data, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});

fs.readFile(process.argv[3], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(process.argv[4], data, err => {
      if (err) {
        console.log(err);
      }
    });
  }
});
