#!/usr/bin/node
exports.esrever = function (list) {
  const ListReverse = [];
  let ListLength = list.length - 1;

  while (ListLength >= 0) {
    ListReverse.push(list[ListLength]);
    ListLength--;
  }
  return (ListReverse);
};
