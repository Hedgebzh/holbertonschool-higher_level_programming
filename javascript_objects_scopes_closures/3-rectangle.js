#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return (undefined);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;

    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
};
/* print() {
  let i = 0
  let y = 0
  let PrintRectangle = '';

  while (i < this.height) {
    while (y < this.weight) {
      PrintRectangle += 'X';
      y++;
    }
    console.log(PrintRectangle);
    i++;
  }
} */
