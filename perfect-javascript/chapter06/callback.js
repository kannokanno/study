// 簡単な実装
var emitter = {
  callbacks:[],
  register:function(fn) {
    this.callbacks.push(fn);
  },
  onOpen:function() {
    for (var i in this.callbacks) {
      this.callbacks[i]();
    };
  },
  reset:function() {
    this.callbacks = [];
  }
}

emitter.register(function(){ print('handler1 is called'); });
emitter.register(function(){ print('handler2 is called'); });
emitter.onOpen();
emitter.reset();

// 状態を持てるようにする

// NG実装
function MyClass(msg) {
  this.msg = msg;
  this.show = function() { print(this.msg + ' is called'); }
}
var listner1 = new MyClass('listner1');
var listner2 = new MyClass('listner2');
emitter.register(listner1.show);
emitter.register(listner2.show);
emitter.onOpen();
// =>
// undefined is called
// undefined is called
// this参照が正しくない。global参照になってしまいundefined
emitter.reset();

// bindを使った対応
emitter.register(listner1.show.bind(listner1));
emitter.register(listner2.show.bind(listner2));
emitter.onOpen();
emitter.reset();


// closureを使うパターン
emitter.register((function(){
  var msg = 'closure1';
  return function() { print(msg + ' is called'); }
})());
emitter.register((function(){
  var msg = 'closure2';
  return function() { print(msg + ' is called'); }
})());
emitter.onOpen();
emitter.reset();
