#Bayes Theorem
#You have two coins in hand. Out of the two, one is a real coin(H & T) and the other is a faulty coin (T & T)
#Pick a random coin with eyes closed. Toss it in the air. The coin lands with T facing upwards.
#Find probability that this is a faulty coin.

#Solution #Bayes Theorem

#P(Head|CoinReal) = 0.5, P(Tail|CoinReal) = 0.5
#P(Head|CoinFaulty) = 0, P(Tail|CoinFaulty) = 1

#P(Head) = 0.5 * 0.5+ 0.5 * 0 = 0.25
#P(Tail) = 0.5 * 0.5+ 0.5 * 1 = 0.75

#P(CoinFaulty) = 0.5
#Conditional Probability using Bayes Theorem
#P(CoinFaulty|Tail) = [P(Tail|CoinFaulty) * P(CoinFaulty) ] / P(Tail)
Numerator = 1 * 0.5
Denominator = 0.75
Probability = Numerator/Denominator

print("P(CoinFaulty|Tail) = ",Probability) #0.667


    
