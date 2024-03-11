#!/usr/bin/node

const [, , arg1] = process.argv;

if (arg1 === undefined) {
  console.log('No argument');
} else {
  console.log(arg1);
}

/*

const firstArgument = process.argv[2];

if (firstArgument === undefined) {
    console.log("No argument");
} else {
    console.log(firstArgument);
}
*/
