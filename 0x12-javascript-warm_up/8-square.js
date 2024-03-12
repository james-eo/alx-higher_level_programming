#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

/*
const size = parseInt(process.argv[2]);

if (!isNaN(size)) {
  let i = 0;
  while (i < size) {
    let row = '';
    let j = 0;
    while (j < size) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
*/
