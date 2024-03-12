#!/usr/bin/node
/*
const [, , arg1, arg2] = process.argv;

if (arg1 === undefined || arg2 === undefined) {
  console.log('Please enter two arguments');
} else {
  console.log(`${arg1} is ${arg2}`);
}
*/

const args = process.argv.splice(2);

if (args.length < 2) {
    console.log("Please provide two arguments");
} else {
    console.log(`${args[0]} is ${args[1]}`);
}
