#!/usr/bin/node

/* Create a method that gives the length of a list */
exports.nbOccurences = function (list, searchElement) {
  const newList = [];
  const lastElement = list.length - 1

  /* Iterate from the end of list to the beginning */
  for (let i = lastElement; i < list.length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
