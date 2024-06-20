#!/usr/bin/node

/* Access first argument */
const firstArg = process.argv[2];

function factorial (n) {
  const numA = parseInt(n);

  if (isNaN(numA)) {
    return 1;
  } else if (numA <= 1) {
    return 1;
  } else {
    return numA * factorial(numA - 1);
  }
}

/* Compute and print the factorial */
console.log(factorial(firstArg));
