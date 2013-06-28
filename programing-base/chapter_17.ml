#use "test.ml"

type sample = Foo of int
            | Bar of string
            | Baz of bool
;;

let show_sample_type data = match data with
    Foo(n) -> print_string ((string_of_int n) ^ "\n")
  | Bar(s) -> print_string (s ^ "\n")
  | Baz(b) -> print_string ((string_of_bool b) ^ "\n")
;;

show_sample_type (Foo(10)) ;;
show_sample_type (Bar("hoge")) ;;
show_sample_type (Baz(true)) ;;


type tree_t = Empty
            | Leaf of int
            | Node of tree_t * int * tree_t
;;


let rec tree_double tree = match tree with
    Empty -> 0
  | Leaf(n) -> n * 2
  | Node(left, n, right) -> (tree_double left) + (n * 2) + (tree_double right)
;;

test_start "tree_double" ;;
test (tree_double Empty) 0 ;;
test (tree_double (Leaf(10))) 20 ;;
test (tree_double (Node (Leaf(10), 5, Empty))) 30 ;;
test (tree_double (Node (Leaf(10), 5, (Node (Leaf(10), 5, Leaf(10)))))) 80 ;;


let rec tree_map f tree = match tree with
    Empty -> Empty
  | Leaf(n) -> Leaf(f n)
  | Node(left, n, right) -> Node ((tree_map f left), (f n), (tree_map f right))
;;

test_start "tree_map" ;;
let tree1 = Empty ;;
let tree2 = Leaf (3) ;;
let tree3 = Node (tree1, 4, tree2) ;;
let tree4 = Node (tree2, 5, tree3) ;;
test (tree_map (fun x -> x) tree1) Empty ;;
test (tree_map (fun x -> x + 1) tree2) (Leaf (4)) ;;
test (tree_map (fun x -> x * 3) tree3) (Node (Empty, 12, Leaf (9))) ;;
test (tree_map (fun x -> x * 2) tree4) (Node (Leaf (6), 10, Node (Empty, 8, Leaf (6)))) ;;


let rec tree_length tree = match tree with
    Empty -> 0
  | Leaf(n) -> 1
  | Node(left, n, right) -> (tree_length left) + 1 + (tree_length right)
;;

test_start "tree_length" ;;
let tree1 = Empty ;;
let tree2 = Leaf (3) ;;
let tree3 = Node (tree1, 4, tree2) ;;
let tree4 = Node (tree2, 5, tree3) ;;
test (tree_length tree1) 0 ;;
test (tree_length tree2) 1 ;;
test (tree_length tree3) 2 ;;
test (tree_length tree4) 4 ;;


let rec tree_depth tree = match tree with
    Empty -> 0
  | Leaf(n) -> 0
  | Node(left, n, right) -> 1 + (max (tree_depth left) (tree_depth right))
;;

test_start "tree_depth" ;;
let tree1 = Empty ;;
let tree2 = Leaf (3) ;;
let tree3 = Node (tree1, 4, tree2) ;;
let tree4 = Node (tree2, 5, tree3) ;;
test (tree_depth tree1) 0 ;;
test (tree_depth tree2) 0 ;;
test (tree_depth tree3) 1 ;;
test (tree_depth tree4) 2 ;;


let rec binary_search tree key = match tree with
    Empty -> false
  | Leaf(n) -> n = key
  | Node(left, n, right) -> if n = key then true
                            else if key < n
                                 then binary_search left key
                                 else binary_search right key
;;


test_start "binary_search" ;;
let tree1 = Empty ;;
let tree2 = Leaf (3) ;;
let tree3 = Node (Leaf (1), 2, Leaf (3)) ;;
let tree4 = Node (Empty, 7, Leaf (9)) ;;
let tree5 = Node (tree3, 6, tree4) ;;
test (binary_search tree1 3) false ;;
test (binary_search tree2 3) true ;;
test (binary_search tree3 3) true ;;
test (binary_search tree3 2) true ;;
test (binary_search tree4 5) false ;;
test (binary_search tree5 1) true ;;
