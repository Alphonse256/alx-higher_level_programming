#!/usr/bin/node
const argumentList = process.argv.slice(2);
const numbers = argumentList.map(args => Number(args));
if (numbers.length < 2) {
  console.log('0');
} else {
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
