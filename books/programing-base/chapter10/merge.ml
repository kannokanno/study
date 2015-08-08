let rec merge lst1 lst2 = match (lst1, lst2) with
    ([], []) -> []
  | (first1 :: rest1, []) -> lst1
  | ([], first2 :: rest2) -> lst2
  | (first1 :: rest1, first2 :: rest2) ->
          if first1 < first2
          then first1 :: merge rest1 lst2
          else first2 :: merge rest2 lst1


let test1 = merge [] [] = []
let test2 = merge [] [1; 2] = [1; 2]
let test3 = merge [1; 2] [] = [1; 2]
let test4 = merge [1; 2; 5] [3; 4; 6] = [1; 2; 3; 4; 5; 6]
