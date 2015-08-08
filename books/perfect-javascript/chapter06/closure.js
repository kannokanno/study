// まずは入れ子の関数
(function(){
  function g() {
    print('g is called');
  }
  g();
})();

// 入れ子の関数とスコープ
(function(){
  var n = 1;
  function g() {
    // スコープチェーンして外側関数へ変数解決にいく
    print('n is ' + n);
    print('g is called');
  }
  g();
})();

// 入れ子の関数を返す
var f = (function(){
  var n = 1;
  function g() {
    print('n is ' + n++);
    print('g is called');
  }
  return g;
})();
f();
f();
f();


// クロージャの注意
function funcs() {
  var fArray = [];
  for (var i = 0; i < 10; i++) {
    fArray.push(function(){ print(i); });
  }
  return fArray;
}
var fArray = funcs();
for (var i in fArray) {
  fArray[i](); // すべて10が出力される。期待値は0から9
};
