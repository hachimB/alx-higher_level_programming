#!/usr/bin/node
let sum = 0;
function add (a, b) {
  return a + b;
}
sum = add(Number(process.argv[2]), Number(process.argv[3]));
console.log(sum);
