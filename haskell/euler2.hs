answer = thisAnswer
  where
    fib :: Int -> Int
    fib n = table !! n
      where
        table = 0 : 1 : zipWith (+) table (tail table)
    thisAnswer = sum [x | x <- takeWhile ( < ((10 ^ 6) * 4)) (map fib [1..]), even x]

main :: IO ()
main = print answer
