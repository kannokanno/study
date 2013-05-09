let second lst = match lst with
  _ :: s :: _ -> s
  | _ -> 0

(* test *)
let test1 = second [] = 0
let test1 = second [1] = 0
let test1 = second [1;2;3] = 2
