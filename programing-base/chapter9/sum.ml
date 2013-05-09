let rec sum lst = match lst with
    [] -> 0
  | first :: rest -> first + sum rest

(* test *)
let test1 = sum [] = 0
let test2 = sum [2] = 2
let test3 = sum [1; 2] = 3
let test4 = sum [1; 2; 3; 4] = 10
