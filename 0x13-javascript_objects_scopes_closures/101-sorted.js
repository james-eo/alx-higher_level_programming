#!/usr/bin/node

const { dict } = require('./101-data');

const occurrenceDict = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!occurrenceDict[occurrences]) {
    occurrenceDict[occurrences] = [];
  }
  occurrenceDict[occurrences].push(userId);
}

console.log(occurrenceDict);
