#!/usr/bin/node

exports.esrever = function (list) {
  /* Reserved list */
  const newList = [];

  /* Iterate from the end of the list to the beginning */
  for (let i = list.length - 1; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
