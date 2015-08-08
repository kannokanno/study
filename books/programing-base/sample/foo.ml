let f a = match a with
    n when n = infinity -> "inf\n"
  | _ -> "other\n"
;;

print_string (f infinity);;
print_string (f 1.0);;
