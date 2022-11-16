#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const uri = `https://swapi-api.hbtn.io/api/films/${args[0]}`;

request(uri, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters_uri = JSON.parse(body).characters;

    characters_uri.forEach(character_uri => {
      request(character_uri, (err, resp, body) => {
        console.log(JSON.parse(body).name);
      });
    });
  }
});
