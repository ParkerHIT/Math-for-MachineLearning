#Bayes Theorem
#Find Probability of an applicant Passing Stats Interview given that they passed the Coding Interview already
#Given Info
#P(StatsPass) = 0.25, P(CodingPass) = 0.4
#P(StatsFail) = 0.75, P(CodingPass) = 0.2

#Solution #Bayes Theorem

#Conditional Probability using Bayes Theorem
#(PassStats|PassCoding) = (#P(PassCoding|PassStats) * #P(PassStats) ) / #P(PassCoding)

#Numerator
#P(PassCoding|PassStats) = 0.4
#P(PassStats)= 0.25
bothpass= 0.25* 0.40
print(bothpass)

#Denominator 
codingpass = (0.25*0.40) + (0.75 * 0.20)
print(codingpass)


statspass_given_codingpass = bothpass/codingpass
print(statspass_given_codingpass)

#(PassStats|PassCoding) = 0.4
    
