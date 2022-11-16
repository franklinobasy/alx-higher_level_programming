#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');

const options = {
  encoding: 'utf8',
  flag: 'w'
};

fs.writeFile(args[0], args[1], options, (err) => {
  if (err) {
    console.error(err);
  }
});
