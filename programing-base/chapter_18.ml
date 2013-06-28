#use "test.ml"

let rec assoc name lst = match lst with
    [] -> raise Not_found
  | (ekimei, kyori) :: rest ->
      if ekimei = name then kyori else assoc name rest
;;

try
  assoc "後楽園" []
with
  Not_found -> print_string (string_of_bool true ^ "\n"); 0.0
;;
test (assoc "後楽園" [("新大塚", 1.2); ("後楽園", 1.8)]) 1.8 ;;
try
  assoc "池袋" [("新大塚", 1.2); ("後楽園", 1.8)]
with
  Not_found -> print_string (string_of_bool true ^ "\n"); 0.0
;;
