#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let occurence = 0;
  while (list[i] != null) {
    if (list[i] === searchElement) {
      occurence += 1;
    }
    i++;
  }
  return (occurence);
};
