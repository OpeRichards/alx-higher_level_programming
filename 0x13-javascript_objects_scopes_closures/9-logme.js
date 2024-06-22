#!/usr/bin/node

/* Declare variable to keep track of the number of arguments printed */
let count = 0;
/* A function that prints the index of argument and it's value */
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
