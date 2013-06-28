#use "ekimei_list.ml"
#use "ekikan_list.ml"

(* ------------------------- *)
let test_mode = true ;;
let test_start s = if test_mode then print_string (s ^ "\n") else ();;
let test a b = if test_mode then
    let _assert a b = string_of_bool (a = b) ^ "\n" in
      print_string (_assert a b)
    else ();;
(* ------------------------- *)

(* ------------------------- *)
let rec romaji_to_kanji romaji lst = match lst with
    [] -> ""
  | {kanji = k; romaji = r} :: rest -> if r = romaji then k
                                                     else romaji_to_kanji romaji rest
;;

test_start "=== Test romaji_to_kanji ===";;
test (romaji_to_kanji "hogee" global_ekimei_list) "";;
test (romaji_to_kanji "myogadani" global_ekimei_list) "茗荷谷";;
(* ------------------------- *)

(* ------------------------- *)
(* String -> String -> [ekikan_t] -> Float *)
let rec get_ekikan_kyori kiten shuten lst = match lst with
    [] -> infinity
  | {kiten = k; shuten = s; kyori = ky} :: rest ->
                            if (kiten = k && shuten = s) || (kiten = s && shuten = k)
                              then ky
                              else get_ekikan_kyori kiten shuten rest
;;

test_start "=== Test get_ekikan_kyori ===";;
test (get_ekikan_kyori "存在しない駅" "茗荷谷" global_ekikan_list) infinity;;
test (get_ekikan_kyori "茗荷谷" "新大塚" global_ekikan_list) 1.2;;
test (get_ekikan_kyori "新大塚" "茗荷谷" global_ekikan_list) 1.2;;
(* ------------------------- *)

(* ------------------------- *)
(* String -> String -> String *)
let rec kyori_wo_hyoji kiten shuten =
  let not_found_string s = s ^ "という駅は存在しません" in
  match (romaji_to_kanji kiten global_ekimei_list, romaji_to_kanji shuten global_ekimei_list) with
    ("", "") -> not_found_string kiten
  | ("", _)  -> not_found_string kiten
  | (_, "")  -> not_found_string shuten
  | (k, s)   -> match get_ekikan_kyori k s global_ekikan_list with
                  inf when inf = infinity -> Printf.sprintf "%s駅と%s駅はつながっていません" k s
                | kyori    -> let kyori_s = string_of_float(kyori) in
                    Printf.sprintf "%s駅から%s駅までは%skmです" k s kyori_s
;;

test_start "=== Test kyori_wo_hyoji ===";;
test (kyori_wo_hyoji "hoge" "piyo") "hogeという駅は存在しません";;
test (kyori_wo_hyoji "hoge" "myogadani") "hogeという駅は存在しません";;
test (kyori_wo_hyoji "shinotsuka" "piyo") "piyoという駅は存在しません";;
test (kyori_wo_hyoji "myogadani" "shinotsuka") "茗荷谷駅から新大塚駅までは1.2kmです";;
test (kyori_wo_hyoji "ikebukuro" "myogadani") "池袋駅と茗荷谷駅はつながっていません";;
(* ------------------------- *)
