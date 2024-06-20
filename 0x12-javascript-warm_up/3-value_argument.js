#!/usr/bin/node

/* Access the first argument passed */
const firstArg = process.argv[2];

/* Check if the argument is provided and print it */
if (firstArg !== undefined) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
