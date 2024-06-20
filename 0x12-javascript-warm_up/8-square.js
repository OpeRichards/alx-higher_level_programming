#!/usr/bin/node

/* Access the first argument passed */
const firstArg = process.argv[2];

/* Print a square first argument times */
const numtimes = parseInt(firstArg);

if (isNaN(numtimes)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numtimes; i++) {
    let row = '';
    for (let j = 0; j < numtimes; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
