Function.prototype.defer = function defer(time) {
  return (a, b) => setTimeout(() => this.call(this, a, b), time);
};

function f(a, b) {
  console.log(a + b);
}

f.defer(1000)(1, 2);
