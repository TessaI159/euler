def find_answer()
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  target = 200
  solutions = [1] + [0] * target
  
  coins.each do |coin|
    (coin..target).each do |i|
      solutions[i] += solutions[i - coin]
    end
  end
  solutions[-1]
end

find_answer
