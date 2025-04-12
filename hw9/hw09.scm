;;; Homework 09: Scheme List, Tail Recursion and Macro

;;; Required Problems

(define (make-change total biggest)
  (if (= total 0)
    (cons nil nil)
    (if (< total 0)
      nil
      (if (= biggest 0)
        nil
        (append (map (lambda (lst1) (cons biggest lst1))
                      (make-change (- total biggest) biggest))
                (make-change total (- biggest 1))))))
)


(define (find n lst)
  (define (find-helper n m lst)
    (if (= n (car lst))
      m
      (find-helper n (+ m 1) (cdr lst))))
  (find-helper n 0 lst)
)


(define (find-nest n sym)
  (define (helper n sym record)
    (if (null? sym)
      #f
      (if (and (list? (car sym)) (list? (cdr sym)))
        (or (helper n (car sym) `(car ,record)) (helper n (cdr sym) `(cdr ,record)))
        (if (= (car sym) n)
          `(car ,record)
          (helper n (cdr sym) `(cdr ,record))))))
  (helper n (eval sym) sym)
)


(define-macro (my/or operands)
  (cond
    ((null? operands) #f)
    ((null? (cdr operands)) (car operands))
    (else
      `(let ((t ,(car operands)))
          (if t
            t
            (my/or ,(cdr operands))))))
)


(define (helper1 args vals indices n)
  (if (null? indices)
    args
    (if (= n (car indices))
      (cons (car vals) (helper1 (cdr args) (cdr vals) (cdr indices) (+ n 1)))
      (cons (car args) (helper1 (cdr args) vals indices (+ n 1)))))
)
(define (helper2 args indices n)
  (if (null? indices)
    args
    (if (= n (car indices))
      (helper2 (cdr args) (cdr indices) (+ n 1))
      (cons (car args) (helper2 (cdr args) indices (+ n 1)))))
)

(define-macro (k-curry fn args vals indices)
  `(lambda ,(helper2 args indices 0) ,(append (list fn) (helper1 args vals indices 0)))
)


(define-macro (let* bindings expr)
  (if (null? bindings)
    `(let () ,expr)
    `(let
      (,(car bindings))
      (let* ,(cdr bindings) ,expr)))
)

;;; Just For Fun Problems


; Helper Functions for you
(define (cadr lst) (car (cdr lst)))
(define (cddr lst) (cdr (cdr lst)))
(define (caddr lst) (car (cdr (cdr lst))))
(define (cdddr lst) (cdr (cdr (cdr lst))))

(define-macro (infix expr)
  'YOUR-CODE-HERE
)


; only testing if your code could expand to a valid expression 
; resulting in my/and/2 and my/or/2 not hygienic
(define (gen-sym) 'sdaf-123jasf/a123)

; in these two functions you can use gen-sym function.
; assumption:
; 1. scm> (eq? (gen-sym) (gen-sym))
;    #f
; 2. all symbol generate by (gen-sym) will not in the source code before macro expansion
(define-macro (my/and/2 operands)
  'YOUR-CODE-HERE
)

(define-macro (my/or/2 operands)
  'YOUR-CODE-HERE
)

