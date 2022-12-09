#!/usr/bin/node

process.argv[2] = process.argv[2] * 1;
process.argv[3] = process.argv[3] * 1;

function add (a, b) {
  const c = a + b;
  return (c);
}

console.log(add(process.argv[2], process.argv[3]));
