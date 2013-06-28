#use "test.ml"

let time2 x = x * 2 ;;
let add3 x = x + 3 ;;

let compose f1 f2 = let g x = f1 (f2 x) in g ;;

test ((compose time2 add3) 4) 14
