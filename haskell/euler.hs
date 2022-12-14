module Euler where


-- Returns True if x is an int, False elsewise
isInt x = x == fromInteger (round x)


sumArithSeq :: Int -> Int -> Int
-- Returns the sum of all numbers divisle by b from 1 to e - 1
sumArithSeq b e = (div (div (e - 1) b * (div (e - 1) b + 1)) 2) * b


triangleNumber :: Int -> Int
-- Returns the nth triangle number
triangleNumber n = div (n^2 + n) 2


pentagonNumber :: Int -> Int
-- Returns the nth pengaton number
pentagonNumber n = div ((3 * n^2) - n) 2


hexagonNumber :: Int -> Int
-- Returns the nth hexagon number
hexagonNumber n = (2 * n^2) - n


sumOfSquares :: Int -> Int
-- Returns the sum of squares from 1 through n
-- If you need the sum of squares from x through n you can use:
-- sumOfSquares n - sumOfSquares (x - 1)
sumOfSquares n = div (n * (n + 1) * ((2 * n) + 1)) 6


squareOfSums :: Int -> Int
-- Returns the square of sums from 1 through n
-- If you need the square of sums from x through n you can use:
-- (sumOfSeq n - sumOfSeq (x - 1))^2
squareOfSums n = (div (n^2 + n) 2)^2


sumOfSeq :: Int -> Int
-- Sum of integers from 1 through n
-- If you need the sum of x through n you can use:
-- sumOfSeq n - sumOfSeq (x - 1)
sumOfSeq n = div (n^2 + n) 2
