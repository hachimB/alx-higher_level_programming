#!/usr/bin/node
let i;
let j;
let reg;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (i = 0; i < Number(process.argv[2]); i++) {
    reg = '';
    for (j = 0; j < Number(process.argv[2]); j++) {
      reg += 'X';
    }
    console.log(reg);
  }
}
