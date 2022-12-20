#!/usr/bin/node

class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  /* Method charPrint(c) */
  charPrint (C) {
    if (typeof C === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
