// bindのサンプル実装
function MyClass(msg) {
  this.msg = msg;
  this.show = function() { print(this.msg + ' is called'); }
}

function _bind(context, fn) {
  return function() {
    return fn.apply(context);
  }
}

function doit(fn) {
  fn();
}

var obj = new MyClass('msg1');
doit(obj.show); // => undefined is called
doit(obj.show.bind(obj)); // => msg1 is called
doit(_bind(obj, obj.show)); // => msg1 is called
