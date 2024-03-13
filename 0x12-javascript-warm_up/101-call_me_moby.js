#!/usr/bin/node
/*
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
*/
exports.callMeMoby = function (x, theFunction) {
  let count = 0;
  while (count < x) {
    theFunction();
    count++;
  }
};
