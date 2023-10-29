integer function sum_arith_seq(b, e) result(r)
  integer, intent (in) :: b, e ! input
  
  integer              :: a, n ! intermediary variables

  a = e - 1
  n = a / b

  r = RSHIFT((n * (n + 1)), 1) * b
end function sum_arith_seq

program euler1
  implicit none
  integer, external :: sum_arith_seq
  integer :: total
  integer, parameter :: n = 1000
  
  total = sum_arith_seq(3,n)
  total = total + sum_arith_seq(5,n)
  total = total - sum_arith_seq(15,n)
  

  print *, total

end program euler1
