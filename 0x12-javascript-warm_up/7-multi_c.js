#!/usr/bin/node

/* Access first argument passed */
const firstArg = process.argv[2];
const toPrint = 'C is fun';

/* Check firstArg is an integer.
    Print string firstArg number of times.
*/
if (typeof firstArg !== 'string' || isNaN(parseInt(firstArg))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(firstArg); i++) {
    console.log(toPrint);
  }
}
