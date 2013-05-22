// newによる生成
function MyClass1(x, y) {
  this.x = x;
  this.y = y;
}
var obj1 = new MyClass1(1, 2);
print(obj1); // => [object Object]
print(obj1.x, obj1.y); // => 1 2
print(this.x, this.y); // => undefined undefined

// newに渡せるのは関数である
// ということは、関数呼び出しをそのまましても同じ結果になるか？
print(MyClass1(1, 2)); // => undefined
// 結果:ならない。戻り値の定義がないので関数呼び出しではundefinedになる

// では明示的にthisをreturnしたらどうか？
function MyClass2(x, y) {
  this.x = x;
  this.y = y;
  return this;
}
print(MyClass2(1, 2)); // => [object global]
// 結果:globalオブジェクトが返される(newの場合はObjectオブジェクト)

// プロパティアクセスはできる
var obj2 = MyClass2(1, 2);
print(obj2.x, obj2.y);
// しかしglobalオブジェクトに追加されたのでthisアクセスで見えてしまう
print(this.x, this.y); // => 1 2

// new式で呼ばれると次のような処理になる
// 1. new式で指定した関数の呼び出し
// 2. 空オブジェクトを生成
// 3. 関数内部のthis参照を2のオブジェクトに付ける
// 4. newの評価値として2のオブジェクトを返す
