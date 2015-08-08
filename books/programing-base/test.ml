(* ------------------------- *)
let test_mode = true ;;
let test_start s = if test_mode then print_string ("=== Test " ^ s ^ " ===\n") else ();;
let test a b = if test_mode then
    let _assert a b = string_of_bool (a = b) ^ "\n" in
      print_string (_assert a b)
    else ();;

let rec string_of_list lst = match lst with
    [] -> ""
  | head :: tail -> head ^ "\n" ^ (string_of_list tail);;

let rec int_of_list lst = match lst with
    [] -> ""
  | head :: tail -> string_of_int(head) ^ "\n" ^ (int_of_list tail);;
(* ------------------------- *)

