#!/usr/bin/node

const [, , arg1, arg2] = process.argv;

if (arg1 === undefined || arg2 === undefined) {
  console.log('Please enter two arguments');
} else {
  console.log(`${arg1} is ${arg2}`);
}
