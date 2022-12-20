#!/usr/bin/node

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  /* Method charPrint(c) */
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
