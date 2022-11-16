#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request
  .get(args[0])
  .on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
  });
