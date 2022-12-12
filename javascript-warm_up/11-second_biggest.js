#!/usr/bin/node

let i = 0;
let j = 0;
let BiggestN = 0;
let SecondBiggestN = 0;

if (process.argv[2] === undefined) {
  console.log(0);
} else if (process.argv[3] === undefined) {
  console.log(0);
} else {
  while (process.argv[i] !== undefined) {
    process.argv[i] = process.argv[i] * 1;
    if (process.argv[i] > BiggestN) {
      BiggestN = process.argv[i];
    }
    i++;
  }
  while (process.argv[j] !== undefined) {
    process.argv[j] = process.argv[j] * 1;
    if (process.argv[j] < BiggestN && process.argv[j] > SecondBiggestN) {
      SecondBiggestN = process.argv[j];
    }
    j++;
  }
  console.log(SecondBiggestN);
}
