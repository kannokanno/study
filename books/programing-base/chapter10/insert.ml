let rec insert lst n = match lst with
    [] -> [n]
  | first :: rest -> if first < n
                        then first :: insert rest n
                        else n :: first :: rest (* = n :: lst *)

(* test *)
let test1 = insert [1] 5 = [1; 5]
let test1 = insert [9] 5 = [5; 9]
let test1 = insert [1; 3; 4; 7; 8] 5 = [1; 3; 4; 5; 7; 8]
