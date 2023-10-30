program euler1
  use euler
  implicit none
  
  integer :: total
  integer, parameter :: n = 1000
  
  total = sum_arith_seq(3,n)
  total = total + sum_arith_seq(5,n)
  total = total - sum_arith_seq(15,n)
  

  print *, total

end program euler1
