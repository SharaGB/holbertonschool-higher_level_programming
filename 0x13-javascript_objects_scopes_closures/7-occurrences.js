#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurrences = 0;
  for (const num in list) {
    if (list[num] === searchElement) {
      occurrences += 1;
    }
  }
  return occurrences;
};
