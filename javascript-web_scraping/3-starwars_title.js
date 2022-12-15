#!/usr/bin/node

const request = require('request');
const UrlConcat = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function callback (error, response, body) {
  if (error != null) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
}

request(UrlConcat, callback);
