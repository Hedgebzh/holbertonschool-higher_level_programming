#!/usr/bin/node

const phrasing = 'C is fun';
let i = 0;

while (i < process.argv[2]) {
  console.log(phrasing);
  i++;
}