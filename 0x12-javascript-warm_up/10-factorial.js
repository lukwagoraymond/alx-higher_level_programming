#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if ((n >= 0) && (n <= 1)) {
    return 1;
  }
  return (n * factorial(n - 1));
}

const args = process.argv;
console.log(factorial(parseInt(args[2])));
