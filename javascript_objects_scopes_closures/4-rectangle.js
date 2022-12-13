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
    let y = 0;
    let PrintRectangle = '';

    while (i < this.height) {
      while (y < this.width) {
        PrintRectangle += 'X';
        y++;
      }
      console.log(PrintRectangle);
      i++;
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    this.storeheight = this.height;
    this.height = this.width;
    this.width = this.storeheight;
  }
};
