#!/usr/bin/node

const add = function (a, b) {
  return a + b;
};

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

const num = add(arg1, arg2);
console.log(`${num}`);

/*
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

const sum = add(arg1, arg2);
console.log(`${sum}`);
*/
