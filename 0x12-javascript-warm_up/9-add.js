#!/usr/bin/node

/* Access the first and second arguments */
const a = process.argv[2];
const b = process.argv[3];

/* Add two integers */
function add (a, b) {
  const numA = parseInt(a);
  const numB = parseInt(b);

  if (isNaN(numA) || isNaN(numB)) {
    return 'NaN';
  } else {
    return numA + numB;
  }
}

/* Print the result of the addition */
console.log(add(a, b));
