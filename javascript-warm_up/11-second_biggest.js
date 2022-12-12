#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log(0);
} else if (process.argv[3] === undefined) {
  console.log(0);
}

let i = 0;
biggest_n = process.argv[2];

while (process.argv[i] != undefined) {
    process.argv[i] = process.argv[i] * 1;
    if (process.argv[i] > biggest_n) {
      biggest_n = process.argv[i];
    }
    i++;
  }
  
  console.log(biggest_n);