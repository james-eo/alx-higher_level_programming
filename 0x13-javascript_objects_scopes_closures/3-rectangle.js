#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const cha = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(cha);
    }
  }
};
