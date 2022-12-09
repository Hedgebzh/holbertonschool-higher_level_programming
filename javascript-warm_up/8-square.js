#!/usr/bin/node

let i = 0;
let y = 0;
let square = '';

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}

while (i < process.argv[2]) {
  square += 'X';
  i++;
}

while (y < process.argv[2]) {
  console.log(square);
  y++;
}
