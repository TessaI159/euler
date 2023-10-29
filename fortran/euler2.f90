program euler2
  integer :: answer, current, previous, temp
  answer = 0
  current = 2
  previous = 1
  temp = 0

  do while (current < 4000000)
     if (MODULO(current,2) == 0) THEN
        answer = answer + current
     end if
     temp = previous
     previous = current
     current = current+temp
  end do

  print *, answer
end program euler2
