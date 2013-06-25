#use "ekimei_list.ml"
#use "ekikan_list.ml"

let test a b = string_of_bool (a = b) ^ "\n" ;;

(* ------------------------- *)
let rec romaji_to_kanji romaji lst = match lst with
    [] -> ""
  | {kanji = k; romaji = r} :: rest -> if r = romaji then k
                                                     else romaji_to_kanji romaji rest
;;

print_string "=== Test romaji_to_kanji ===\n" ;;
print_string (test (romaji_to_kanji "hogee" global_ekimei_list) "") ;;
print_string (test (romaji_to_kanji "myogadani" global_ekimei_list) "茗荷谷") ;;
(* ------------------------- *)
