(defun test2 (ls)
  (print ls)
  (if ls
    (test2 (cdr ls))
    'empty))


(defun test (arg)
  (equalp "a" arg))

(print (test "A"))

