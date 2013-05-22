// Javaと異なり、関数スコープは宣言した行とは無関係
// Java -> 変数宣言した行以降からスコープ有効
// Js   -> どこで定義しようと関数全域
var x = 1;
function f() {
  // globalのxが参照されるわけではない
  print(x); // => undefined
  var x = 2;
  print(x); // => 2
}
f();

// 上記は以下コードと等価である
function f2() {
  var x;
  print(x);
  x = 2;
  print(x);
}
f2();
