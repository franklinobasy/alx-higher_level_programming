#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const request = require('request');

const options = {
  encoding: 'utf8',
  flag: 'w'
};

request
  .get(args[0])
  .pipe(fs.createWriteStream(args[1]), options);
