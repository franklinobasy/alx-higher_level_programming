#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const uri = args[0];

request(uri, (err, resp, body) => {
  if (err) {
    console.err(err);
  } else {
    const results = JSON.parse(body).results;
    let n = 0;

    results.forEach(result => {
      const characters = result.characters;

      characters.forEach(character => {
        if (character.endsWith('18/')) {
          n++;
        }
      });
    });
    console.log(n);
  }
});
