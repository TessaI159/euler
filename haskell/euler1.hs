answer = sumArithSeq 3 1000 + sumArithSeq 5 1000 - sumArithSeq 15 1000
  where
    sumArithSeq :: Int -> Int -> Int
    sumArithSeq b e = ((div (e - 1) b * (div (e - 1) b + 1)) `div` 2) * b



main :: IO ()
main = print answer
