module euler
  implicit none
  private
  public :: sum_arith_seq, is_prime, prime_factors

contains
  integer function sum_arith_seq(b, e)
    implicit none
    integer, intent (in) :: b, e ! input
    integer              :: a, n ! intermediary variables
  
    a = e - 1
    n = a / b
  
    sum_arith_seq = RSHIFT((n * (n + 1)), 1) * b
  end function sum_arith_seq

  logical function is_prime(n)
    implicit none
    integer, intent (in) :: n
    integer :: i

    is_prime = .true.
    
    if (n < 2) then
       is_prime = .true.
    end if

    
    if (n == 2) then
       is_prime = .true.
    else if (modulo(n,2) == 0) then
       is_prime = .false.
    else
       do i = 2, int(sqrt(real(n,4)) + 1)
          if (modulo(n,i) == 0) then
             is_prime = .false.
          end if
       end do
    end if
  end function is_prime

  
end module euler

