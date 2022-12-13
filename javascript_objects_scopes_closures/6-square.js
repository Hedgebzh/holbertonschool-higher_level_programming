#!/usr/bin/node
const Square2 = require('./5-square.js');

module.exports = class Square extends Square2 {
  charPrint (c) {
    let i = 0;
    let y = 0;
    let PrintSquare = '';

    if (c === undefined) {
      c = 'X';
    }
    while (i < this.height) {
      while (y < this.width) {
        PrintSquare += c;
        y++;
      }
      console.log(PrintSquare);
      i++;
    }
  }
};
