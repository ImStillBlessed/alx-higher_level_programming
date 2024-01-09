#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurance = 0;
  list.forEach(element => {
    if (element === searchElement) occurance += 1;
  });
  return (occurance);
};
