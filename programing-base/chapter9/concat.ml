let rec concat lst = match lst with
    [] -> ""
  | first :: rest -> first ^ concat rest

(* test *)
let test1 = concat [] = ""
let test2 = concat ["a"] = "a"
let test3 = concat ["a"; "b"] = "ab"
let test4 = concat ["a"; "b"; "C"; "D"] = "abCD"

