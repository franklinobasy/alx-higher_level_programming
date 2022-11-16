#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

request(args[0], (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const completed = {};

    const tasks = JSON.parse(body);
    tasks.forEach(task => {
      if (completed[task.userId.toString()]) {
        if (task.completed) {
          completed[task.userId.toString()]++;
        }
      } else {
        if (task.completed) {
          completed[task.userId.toString()] = 1;
        }
      }
    });
    console.log(completed);
  }
});
