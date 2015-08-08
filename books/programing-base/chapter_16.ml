#use "test.ml"

let sum_list lst =
  let rec sum_list_acc _lst acc = match _lst with
      [] -> []
    | head :: tail -> let total = head + acc in
                        total :: sum_list_acc tail total
  in sum_list_acc lst 0
;;

test (sum_list []) [] ;;
test (sum_list [1]) [1] ;;
test (sum_list [3; 2; 1; 4]) [3; 5; 6; 10] ;;


let reverse lst =
  let rec rev rest result = match rest with
      [] -> result
    | head :: tail -> rev tail (head :: result)
  in rev lst []
;;

test (reverse []) [] ;;
test (reverse [1]) [1] ;;
test (reverse [1; 2; 3; 4; 5]) [5; 4; 3; 2; 1] ;;


let rec fold_left f acc lst = match lst with
    [] -> acc
  | head :: tail -> fold_left f (f acc head) tail
;;

test (fold_left (-) 0 []) 0 ;;
test (fold_left (-) 10 [4; 1; 3]) 2 ;;
test (fold_left (fun lst a -> a :: lst) [] [1; 2; 3; 4]) [4; 3; 2; 1] ;;
