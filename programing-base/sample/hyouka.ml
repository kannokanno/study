type gakusei_t = {
  namae : string;
  tensuu : int;
  seiseki : string;
}

(* hyouka : gakusei_t -> gakusei_t *)
let hyouka gakusei = match gakusei with
  {namae = n; tensuu = t; seiseki = s} ->
    {namae = n;
      tensuu = t;
      seiseki = if t >= 80 then "A"
                else if t >= 70 then "B"
                else if t >= 60 then "C"
                else "D"
    }

(* test *)
let test1 = hyouka {namae = "kanno"; tensuu = 90; seiseki = ""}
                  = {namae = "kanno"; tensuu = 90; seiseki = "A"}
let test2 = hyouka {namae = "kanno"; tensuu = 80; seiseki = ""}
                  = {namae = "kanno"; tensuu = 80; seiseki = "A"}
let test3 = hyouka {namae = "kanno"; tensuu = 75; seiseki = ""}
                  = {namae = "kanno"; tensuu = 75; seiseki = "B"}
let test4 = hyouka {namae = "kanno"; tensuu = 70; seiseki = ""}
                  = {namae = "kanno"; tensuu = 70; seiseki = "B"}
let test5 = hyouka {namae = "kanno"; tensuu = 65; seiseki = ""}
                  = {namae = "kanno"; tensuu = 65; seiseki = "C"}
let test6 = hyouka {namae = "kanno"; tensuu = 60; seiseki = ""}
                  = {namae = "kanno"; tensuu = 60; seiseki = "C"}
let test7 = hyouka {namae = "kanno"; tensuu = 55; seiseki = ""}
                  = {namae = "kanno"; tensuu = 55; seiseki = "D"}
