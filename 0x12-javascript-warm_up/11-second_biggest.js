#!/usr/bin/node

/* Count number of arguments passed */
const argCount = process.argv.length - 2;
const args = process.argv.slice(2).map(Number);

/* Search for the second biggest number */
if (argCount <= 1) {
  console.log(0);
} else {
  /* Initialize the highest and second highest numbers */
  let highest = -Infinity;
  let secondHighest = -Infinity;

  /* Loop through the arguments */
  /* Find the highest and second highest numbers */
  for (const num of args) {
    if (num > highest) {
      secondHighest = highest;
      highest = num;
    } else if (num > secondHighest && num !== highest) {
      secondHighest = num;
    }
  }

  /* Print the second highest number */
  console.log(secondHighest);
}
