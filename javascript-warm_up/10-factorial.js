#!/usr/bin/node

process.argv[2] = process.argv[2] * 1;

function factorial (a) {
  if (a > 0) {
    return (a * factorial(a - 1));
  } else {
    return (1);
  }
}

console.log(factorial(process.argv[2]));
