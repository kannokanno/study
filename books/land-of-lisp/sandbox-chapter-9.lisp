;   i i i i i i i       ooooo    o        ooooooo   ooooo   ooooo
;   I I I I I I I      8     8   8           8     8     o  8    8
;   I  \ `+' /  I      8         8           8     8        8    8
;    \  `-+-'  /       8         8           8      ooooo   8oooo
;     `-__|__-'        8         8           8           8  8
;         |            8     o   8           8     o     8  8
;   ------+------       ooooo    8oooooo  ooo8ooo   ooooo   8
;
; Welcome to GNU CLISP 2.49 (2010-07-07) <http://clisp.cons.org/>
;
; Copyright (c) Bruno Haible, Michael Stoll 1992, 1993
; Copyright (c) Bruno Haible, Marcus Daniels 1994-1997
; Copyright (c) Bruno Haible, Pierpaolo Bernardi, Sam Steingold 1998
; Copyright (c) Bruno Haible, Sam Steingold 1999-2000
; Copyright (c) Sam Steingold, Bruno Haible 2001-2010
;
; Type :h and hit Enter for context help.
;
; [1]> (make-array 3)
; #(NIL NIL NIL)
; [2]> (defparameter x (make-array 3))
; X
; [3]> (aref x 1)
; NIL
; [4]> (x)
;
; *** - EVAL: undefined function X
; The following restarts are available:
; USE-VALUE      :R1      Input a value to be used instead of (FDEFINITION 'X).
; RETRY          :R2      Retry
; STORE-VALUE    :R3      Input a new value for (FDEFINITION 'X).
; ABORT          :R4      Abort main loop
; Break 1 [5]> :q
; [6]> (princ x)
; #(NIL NIL NIL)
; #(NIL NIL NIL)
; [7]> (setf (aref x 1) 'foo)
; FOO
; [8]> x
; #(NIL FOO NIL)
; [9]> (setf (aref x 0) 'foo)
; FOO
; [10]> x
; #(FOO FOO NIL)
; [11]> (setf (aref x 5) 'foo)
;
; *** - SYSTEM::STORE: index 5 for #(FOO FOO NIL) is out of range
; The following restarts are available:
; ABORT          :R1      Abort main loop
; Break 1 [12]> :q
; [13]> (setf foo (list 'a 'b 'c))
; (A B C)
; [14]> (second foo)
; B
; [15]> (setf (second foo) 'hoge)
; HOGE
; [16]> foo
; (A HOGE C)
; [17]> (defparameter h (make-hash-table))
; H
; [18]> h
; #S(HASH-TABLE :TEST FASTHASH-EQL)
; [19]> (gethash 'foo h)
; NIL ;
; NIL
; [20]> (setf (gethash 'foo h) "yeah")
; "yeah"
; [21]> h
; #S(HASH-TABLE :TEST FASTHASH-EQL (FOO . "yeah"))
; [22]> (gethash 'foo h)
; "yeah" ;
; T
; [23]> (defun foo () (values 3 7))
; FOO
; [24]> (foo)
; 3 ;
; 7
; [25]> (+ (foo) 10)
; 13
; [26]> (multiple-value-bind (a b) (foo) (+ a b))
; 10
; [27]> (multiple-value-bind (a) (foo) (+ a 1))
; 4
; [28]> 
;
; [63]> (add "hoge" "piyo")
; "hogepiyo"
; [64]> (add 1 2)
;
; *** - NO-APPLICABLE-METHOD: When calling #<STANDARD-GENERIC-FUNCTION ADD> with
;       arguments (1 2), no method is applicable.
; The following restarts are available:
; RETRY          :R1      try calling ADD again
; RETURN         :R2      specify return values
; ABORT          :R3      Abort main loop
; Break 1 [65]> :q
; [66]> (defmethod add ((a number) (b number)) (+ a b))
; WARNING: The generic function #<STANDARD-GENERIC-FUNCTION ADD> is being modified,
;          but has already been called.
; #<STANDARD-METHOD (#<BUILT-IN-CLASS NUMBER> #<BUILT-IN-CLASS NUMBER>)>
; [67]> (add 1 2)
; 3
; [68]> 
