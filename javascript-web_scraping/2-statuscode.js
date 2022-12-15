#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error != null) {
    console.error('error:', error);
  }
  console.log('Code:', response && response.statusCode);
});
