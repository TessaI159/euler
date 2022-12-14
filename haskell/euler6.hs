answer = squareOfSums 100 - sumOfSquares 100
  where
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



main :: IO ()
main = print answer
