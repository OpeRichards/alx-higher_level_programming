#!/usr/bin/node

/* Access the two arguments passed */
const firstArg = process.argv[2];
const secondArg = process.argv[3];

/* Concatenate is in  middle of these arguments */
if (firstArg !== undefined && secondArg !== undefined) {
  console.log(firstArg + ' is ' + secondArg);
} else if (firstArg !== undefined && secondArg === undefined) {
  console.log(firstArg + ' is ' + 'undefined');
} else {
  console.log('undefined is undefined');
}
