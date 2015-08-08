type person1_t = {
  name : string;
  age : int;
}

type person2_t = {
  name : string;
  age : int;
}

let get_age person = match person with
  {age = n} -> n


(* test *)
let test = get_age {name="hoge"; age=15} = 15
