#!/usr/bin/node

const args = process.argv;
const arrLen = args.length;

if (arrLen <= 3) {
  console.log(0);
} else {
  const argz = args.map(Number).slice(2, arrLen).sort((a, b) => a - b);
  console.log(argz[argz.length - 2]);
}
