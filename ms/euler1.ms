// If we list all the natural numbers below 10 that are multiples of 3 or 5, wwe get 3, 5, 6, and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

// O(n) solution
naiveSolution = function(limit)
  total = 0
  for i in range(1,limit-1)
    if i % 3 == 0 or i % 5 == 0 then
      total = total + i
    end if
  end for
  return total
end function

// Returns the sum of all multiples of b below a
sumArithSeq = function(b,e)
  return floor((floor((e-1) / b) * (floor((e-1) / b) + 1)) / 2) * b
end function

// O(1) solution
quickSolution = function(total)
  return sumArithSeq(3, total) + sumArithSeq(5, total) - sumArithSeq(15, total)
end function

// print naiveSolution(1000)
startTime = time
print quickSolution(1000)
endTime = time

print "Time to execute in seconds: " + (endTime - startTime)