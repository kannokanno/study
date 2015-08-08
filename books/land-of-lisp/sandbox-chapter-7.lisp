; ドットリスト
(let ((pair (cons 1 2)))
  (print pair)
  (print (car pair))
  (print (cdr pair))
  (print (car (cons 1 (cons 2 nil))))
  (print (cdr (cons 1 (cons 2 nil))))
  )

; 循環リスト
(setf *print-circle* t)
(defparameter *foo* '(1 2 3))
(setf (cdddr *foo*) *foo*)
(print *foo*)

; 連想リスト
(defparameter *books* '((java . 400)
                        (ruby . 1000)))
(print (assoc 'ruby *books*))
(push '(ruby . 50) *books*)
(print (assoc 'ruby *books*))
(print *books*)

(print '((foo 10)))
(print (assoc 'foo '((foo 10))))

; リストにもsubstitute-ifが使える
(print (substitute-if 0 #'oddp '(1 2 3 4 5)))
(print (alphanumericp #\a))
(print (substitute-if #\_ (complement #'alphanumericp) (prin1-to-string '(1 2 3))))
(print (substitute-if #\_ #'alphanumericp (prin1-to-string '(1 2 3))))
