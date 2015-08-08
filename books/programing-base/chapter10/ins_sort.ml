let rec ins_sort lst = match lst with
    [] -> []
  | first :: rest -> insert (ins_sort rest) first

(* test *)
let test1 = ins_sort [1; 2] = [1; 2]
let test2 = ins_sort [2; 1] = [1; 2]
let test3 = ins_sort [3; 4; 1; 8; 7] = [1; 3; 4; 7; 8]

