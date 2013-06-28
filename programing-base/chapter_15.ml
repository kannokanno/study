#use "test.ml"

let take operator base lst = List.filter (fun item -> operator item base) lst ;;

test (take (<) 3 [1; 3; 2; 4; 5]) [1; 2] ;;
test (take (>) 3 [1; 3; 2; 4; 5]) [4; 5] ;;

let rec quick_sort lst = match lst with
    [] -> []
  | head :: tail -> quick_sort (take (<) head tail)
                    @ [head]
                    @ quick_sort (take (>) head tail)
;;

test_start "quick_sort" ;;
test (quick_sort []) [] ;;
test (quick_sort [1]) [1] ;;
test (quick_sort [3; 1]) [1; 3] ;;
test (quick_sort [1; 3; 2; 4; 5]) [1; 2; 3; 4; 5] ;;


let rec gcd m n = match n with
    0 -> m
  | n -> gcd n (m mod n)
;;

test_start "gcd" ;;
test (gcd 7 5) 1 ;;
test (gcd 30 18) 6 ;;
test (gcd 36 24) 12 ;;

let rec sieve lst = match lst with
    [] -> []
  | one :: [] -> [one]
  | head :: tail -> head :: sieve(List.filter (fun item -> item mod head != 0) tail)
;;

test_start "sieve" ;;
test (sieve [2]) [2] ;;
test (sieve [2; 3; 4; 5; 6; 7]) [2; 3; 5; 7] ;;


let rec prime len = let rec range start last =
  if start > last then [] else start :: range(start + 1) last in
  sieve (range 2 len)
;;

test_start "prime" ;;
test (prime 2) [2] ;;
test (prime 10) [2; 3; 5; 7] ;;
