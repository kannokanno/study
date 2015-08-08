#use "test.ml"

let even x = x mod 2 = 0 ;;
let twice x = x * 2 ;;


test_start "even" ;;
test (even 2) true ;;
test (even 1) false ;;

let rec my_filter predicate lst = match lst with
    [] -> []
  | head :: tail -> if predicate head
                     then head :: my_filter predicate tail
                     else my_filter predicate tail
;;

test_start "my_filter" ;;
test (my_filter even [1; 2; 3]) [2] ;;
test (my_filter even [1; 3]) [] ;;

(* sum *)
let rec my_sum lst = match lst with
    [] -> 0
  | head :: tail -> head + (my_sum tail)
;;

test_start "my_sum" ;;
test (my_sum []) 0 ;;
test (my_sum [1; 2; 3]) 6 ;;

(* length *)
let rec my_length lst = match lst with
    [] -> 0
  | head :: tail -> 1 + (my_length tail)
;;

test_start "my_length" ;;
test (my_length []) 0 ;;
test (my_length [1; 2; 3]) 3 ;;

(* append *)
let rec my_append first second = match first with
    [] -> second
  | head :: tail -> head :: my_append tail second
;;

test_start "my_append" ;;
test (my_append [] [1; 2]) [1; 2] ;;
test (my_append [1; 2] []) [1; 2] ;;
test (my_append [1; 2] [3; 4]) [1; 2; 3; 4] ;;

(* map *)
let rec my_map fn lst = match lst with
    [] -> []
  | head :: tail -> (fn head) :: my_map fn tail
;;

test_start "my_map" ;;
test (my_map twice []) [] ;;
test (my_map twice [1; 2]) [2; 4] ;;

(* fold_r *)
let rec my_fold_r fn lst init = match lst with
    [] -> init
  | head :: tail -> fn head (my_fold_r fn tail init)
;;

test_start "my_fold_r - filter" ;;
let filter_fun predicate =
    let g head tail = if predicate head
                      then head :: tail
                      else tail in g
;;
test (my_fold_r (filter_fun even) [] []) [] ;;
test (my_fold_r (filter_fun even) [1; 2; 3] []) [2] ;;
test (my_fold_r (filter_fun even) [1; 3] []) [] ;;
test_start "my_fold_r - sum" ;;
test (my_fold_r (fun head tail -> head + tail) [] 0) 0 ;;
test (my_fold_r (fun head tail -> head + tail) [1; 2; 3] 0) 6 ;;
test (my_fold_r (+) [1; 2; 3] 0) 6 ;;
test_start "my_fold_r - length" ;;
test (my_fold_r (fun head tail -> 1 + tail) [] 0) 0 ;;
test (my_fold_r (fun head tail -> 1 + tail) [1; 2; 3] 0) 3 ;;
test_start "my_fold_r - append" ;;
test (my_fold_r (fun head tail -> head :: tail) [] [1; 2]) [1; 2] ;;
test (my_fold_r (fun head tail -> head :: tail) [1; 2] []) [1; 2] ;;
test (my_fold_r (fun head tail -> head :: tail) [1; 2] [3; 4]) [1; 2; 3; 4] ;;
test_start "my_fold_r - map" ;;
test (my_fold_r (fun head tail -> twice head :: tail) [] []) [] ;;
test (my_fold_r (fun head tail -> twice head :: tail) [1; 2] []) [2; 4] ;;
