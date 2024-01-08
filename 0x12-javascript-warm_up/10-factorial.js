#!/usr/bin/node
const args = process.argv.slice(2);
let argument = Number(args[0])
function factorial (num) {
  if (num <= 1 || isNaN(num)) {
    return (1);
  }
  return (num * factorial(num - 1));
};
console.log(factorial(argument));