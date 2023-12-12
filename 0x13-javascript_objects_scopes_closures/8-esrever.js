#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let j;
  for (i = 0, j = list.length - 1; i < j; i++, j--) {
    let x = true;
    x = list[i];
    list[i] = list[j];
    list[j] = x;
  }
  return (list);
};
