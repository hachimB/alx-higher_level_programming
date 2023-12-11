#!/usr/bin/node
let i;
const arr = process.argv.slice(2);
for (i = 0; i < arr.length; i++) {
  arr[i] = Number(arr[i]);
}
// sorting in descending order
arr.sort(function (a, b) {
  return b - a;
});

if (arr.length < 2) {
  console.log(0);
} else {
  console.log(arr[1]);
}
