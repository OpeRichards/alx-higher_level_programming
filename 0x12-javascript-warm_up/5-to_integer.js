#!/usr/bin/node

/* Access the first argument passed */
const firstArg = process.argv[2];

/* Print first argument converted in integer */
if (typeof firstArg !== 'string' || isNaN(parseInt(firstArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(firstArg));
}
