// ブロックスコープを作るletはECMA5版にはなく、JSの独自構文
// 使いたいけど、積極的に使ってもいいんだろうか？

// let定義
(function() {
  print("let定義1");
  let x = 1;
  print(x); // => 1
  {
    let x = 2;
    print(x); // => 2
  }
  print(x); // => 1
})();

(function() {
  print("let定義2");
  let x = 1;
  print(x); // => 1
  {
    print(x); // => undefined(varの時と同じ)
    let x = 2;
    print(x); // => 2
  }
  print(x); // => 1
})();

// let文
(function() {
  print("let文1");
  let x = 1;
  print(x); // => 1
  let(x = 2) {
    print(x); // => 2
  }
  print(x); // => 1
})();

(function() {
  print("let文2");
  let x = 1;
  print(x); // => 1
  let(x = 2) {
    print(x); // => 2
    x = 3;
    print(x); // => 3
  }
  print(x); // => 1
})();

(function() {
  print("let式");
  let x = 1;
  print(x); // => 1
  let y = let(x = 2) x + 1;
  print(y); // => 3
  print(x); // => 1
})();

print("END");
print(this.x); // => undefined(グローバル定義になっていないか確認)
