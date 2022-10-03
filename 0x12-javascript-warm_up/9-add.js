#!/usr/bin/node

function add (a, b) {
  const c = a + b;
  console.log(c);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
