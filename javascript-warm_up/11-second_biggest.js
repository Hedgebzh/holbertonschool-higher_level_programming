#!/usr/bin/node

let i = 0;
let j = 0;
let biggest_n = 0;
let second_biggest_n = 0;

if (process.argv[2] === undefined) {
  console.log(0);
} else if (process.argv[3] === undefined) {
  console.log(0);
} else {
    while (process.argv[i] != undefined) {
      process.argv[i] = process.argv[i] * 1;
      if (process.argv[i] > biggest_n) {
        biggest_n = process.argv[i];
      }
      i++;
    }
    while (process.argv[j] != undefined) {
        process.argv[j] = process.argv[j] * 1;
        if (process.argv[j] < biggest_n && process.argv[j] > second_biggest_n) {
            second_biggest_n = process.argv[j];
        }
        j++
    }
}
console.log(second_biggest_n);
