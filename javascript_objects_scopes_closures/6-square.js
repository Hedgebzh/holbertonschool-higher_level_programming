#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
  charPrint(c) {
    let i = 0;
    let y = 0;
    let PrintSquare = '';

    if (c === undefined) {
      c = 'X';
    }
    while (i < this.size) {
      while (y < this.size) {
      PrintSquare += c
      y++
      }
      console.log(PrintSquare)
      i++
    }
  }
};