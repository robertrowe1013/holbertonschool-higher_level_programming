#!/usr/bin/node
var https = require('https');

https.get(process.argv[2], function (res) {
  console.log('code: ', res.statusCode);
}).on('error', function (e) {
  console.error(e);
});
