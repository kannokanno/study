let rec length lst = match lst with
    [] -> 0
  | _ :: rest -> 1 + length rest

(* test *)
let test1 = length [] = 0
let test2 = length [2] = 1
let test3 = length [1; 2] = 2
let test4 = length [1; 2; 3; 4] = 4

