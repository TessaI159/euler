function sum_arith_seq(b, e)
    # (n(n+1))/2
    ((((e-1) ÷ b) * (((e-1) ÷ b) + 1)) ÷ 2) * b
end

start = time()
println("$(sum_arith_seq(3,1000) + sum_arith_seq(5, 1000) - sum_arith_seq(15, 1000))")
duration = time() - start
println(round.(duration; digits=6))


