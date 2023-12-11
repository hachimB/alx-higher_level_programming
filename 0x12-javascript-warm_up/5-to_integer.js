#!/usr/bin/node
if (!process.argv[2] || !/\d/.test(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log(Number(process.argv[2]));
}
