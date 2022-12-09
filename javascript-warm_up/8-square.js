#!/usr/bin/node

let i = 0;
let y = 0;
let square = '';

while (i < process.argv[2]) {
  square += 'X';
  i++;
}

while (y < process.argv[2]) {
  console.log(square);
  y++;
}

