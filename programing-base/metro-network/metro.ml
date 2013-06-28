#use "ekimei_list.ml"
#use "ekikan_list.ml"
#use "eki_t.ml"

(* ------------------------- *)
let test_mode = true ;;
let test_start s = if test_mode then print_string (s ^ "\n") else ();;
let test a b = if test_mode then
    let _assert a b = string_of_bool (a = b) ^ "\n" in
      print_string (_assert a b)
    else ();;

let rec string_of_list lst = match lst with
    [] -> ""
  | s :: rest -> s ^ "\n" ^ (string_of_list rest);;
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

(* ------------------------- *)
(* [ekimei_t] -> [eki_t] *)
let rec make_eki_list ekimei_list = match ekimei_list with
    [] -> []
  | {kanji = k} :: rest -> {namae = k; saitan_kyori = infinity; temae_list = []} :: make_eki_list rest
;;

let rec show_eki_list lst = match lst with
    [] -> ""
  | {namae = n} :: rest -> n ^ "\n" ^ show_eki_list rest
;;
(*
print_string (show_eki_list (make_eki_list global_ekimei_list))
*)
let global_eki_list = make_eki_list global_ekimei_list
(* ------------------------- *)

(* ------------------------- *)
(* [eki_t] -> String -> [eki_t] *)
let rec shokika eki_list kiten = match eki_list with
    [] -> []
  | ({namae = n; saitan_kyori = s; temae_list = tl} as first) :: rest ->
      if n = kiten
      then {namae = n; saitan_kyori = 0.0; temae_list = [n]} :: shokika rest kiten
      else first :: shokika rest kiten
;;

(*
*)
(* ------------------------- *)

(* ------------------------- *)
(* [ekimei_t] -> ekimei_t -> [ekimei_t] *)
(* ekimei_insert : ekimei_t list -> ekimei_t -> ekimei_t list *)
let rec ekimei_insert lst ekimei0 = match lst with
    [] -> [ekimei0] 
  | ({kanji = k; kana = a; romaji = r; shozoku = s} as ekimei) :: rest -> match ekimei0 with
      {kanji = k0; kana = a0; romaji = r0; shozoku = s0} ->
        if a = a0
        then ekimei_insert rest ekimei0
        else
          if a < a0
          then ekimei :: ekimei_insert rest ekimei0
          else ekimei0 :: lst
(*
*)
(* ------------------------- *)

(* ------------------------- *)
(* seiretsu : [ekimei_t] -> [ekimei_t] *)
let rec seiretsu ekimei_list = match ekimei_list with
    [] -> []
  | first :: rest -> ekimei_insert (seiretsu rest) first

(*
*)
(* ------------------------- *)

(* ダイクストラがきちんと理解できていないこともあって、飽きてきた *)
