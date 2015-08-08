// this参照の規則

// コンストラクタ:生成したオブジェクト
function MyClass1() {
  print(this);
}
var a = new MyClass1(); // => [object Object]


// メソッド呼び出し:レシーバオブジェクト
function MyClass2() {
  this.doit = function() { print(this); }
}

var a = new MyClass2();
a.doit(); // => [object Object]

var obj = {f: function() {print(this);}}
obj.f(); // => [object Object]

// メソッド呼び出しでなくなると、thisの解決も変わるので注意
var f = obj.f;
f(); // => [object global]


// apply/call:指定したオブジェクト
function func1() {
  print(this);
}
func1({}); // => [object global]
func1.apply({}); // => [object Object]
func1.call({}); // => [object Object]


// それ以外:globalオブジェクト
function func2() {
  print(this);
}
var a = func2(); // => [object global]

