function Factorial(max) {
  this.max = max;
}

function FactorialIterator(factorial) {
  this.max = factorial.max;
  this.count = this.current = 1;
}

FactorialIterator.prototype.next = function() {
  if (this.count > this.max) {
    throw StopIteration;
  } else {
    return this.current *= this.count++;
  }
}

Factorial.prototype.__iterator__ = function() {
  return new FactorialIterator(this);
}

for (var n in new Factorial(5)) {
  print(n);
}
