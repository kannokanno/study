let rec even lst = match lst with
    [] -> []
  | first :: rest -> if first mod 2 = 0 then first :: even rest
                                        else even rest

(* test *)
let test1 = even [] = []
let test1 = even [2] = [2]
let test1 = even [1; 2] = [2]
let test1 = even [1; 2; 3; 4] = [2; 4]


