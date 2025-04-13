(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  (define (helper lst1 lst2 n)
    (if (null? lst1)
      lst2
      (helper (cdr lst1) (append lst2 (list (list n (car lst1)))) (+ n 1))))
  (helper s (list) 0)
)

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to INORDER? and return
;; the merged lists.
(define (merge inorder? list1 list2)
  (define (helper lst0 lst1 lst2 inorder?)
    (cond
      ((and (null? lst1) (null? lst2)) lst0)
      ((null? lst1) (helper (append lst0 (list (car lst2))) lst1 (cdr lst2) inorder?))
      ((null? lst2) (helper (append lst0 (list (car lst1))) (cdr lst1) lst2 inorder?))
      (else (if (inorder? (car lst1) (car lst2))
        (helper (append lst0 (list (car lst1)) (list (car lst2))) (cdr lst1) (cdr lst2) inorder?)
        (helper (append lst0 (list (car lst2)) (list (car lst1))) (cdr lst1) (cdr lst2) inorder?)))))
  (helper (list) list1 list2 inorder?)
)

(if (and (null? lst1) (null? lst2))
      lst0
      (if (null? lst1)
        )
      (if (inorder? (car lst1) (car lst2))
        (helper (append lst0 (list (car lst1)) (list (car lst2))) (cdr lst1) (cdr lst2) inorder?)
        (helper (append lst0 (list (car lst2)) (list (car lst1))) (cdr lst1) (cdr lst2) inorder?))))

;; Optional Problem 1

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 17
           'replace-this-line
           ; END PROBLEM 17
           ))
        (else
         ; BEGIN PROBLEM 17
         'replace-this-line
         ; END PROBLEM 17
         )))



;; Problem 21 (optional)
;; Draw the hax image using turtle graphics.
(define (hax d k)
  ; BEGIN Question 21
  'replace-this-line
  )
  ; END Question 21