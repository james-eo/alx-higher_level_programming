#!/usr/bin/node

const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

/*
const { argv } = process;
if (argv.length < 3) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

const numOfArgs = process.argv.length - 2;

if (numOfArgs === 0) {
  console.log('No argument');
} else if (numOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
*/
