#!/usr/bin/node
function (x, theFunction) {
  if (x === 0) return;
  theFunction(x -1, theFunction);
}
