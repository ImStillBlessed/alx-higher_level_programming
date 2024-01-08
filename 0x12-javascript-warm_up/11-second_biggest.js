#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  let biggest = Number(args[0]);
  let secondBiggest = Number(args[1]);
  args.forEach(element => {
    const num = Number(element);
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num < biggest) {
      secondBiggest = num;
    }
  });
  console.log(secondBiggest);
}