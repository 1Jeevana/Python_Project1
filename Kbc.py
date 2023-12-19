Ques=["1.What is the largest animal in the world? a.elephant b.giraffe c.blue d.whale", 
   " 2.What is the name of the worlds highest mountain? a.Alps b.Zugspitze c.Annapurna d.Mount Everest ",
    "3.How many wings does a butterfly have? a.4 b.2 c.6 d.5",
   "4.At what age do teenagers become an adult in the UK? a.16 b.18 c.20 d.21",
   " 5.What is the capital city of Scotland?   a.Glasgow b.London c.Europe d.Edinburgh",
  " 6.How many players are there in a football team?  a.9 b.10 c.11 d.12",
    "7.A lobster has how many legs? a.10 b.8 c.21 d.4",
   " 8.What is the shape of Harry Potters scar on his forehead? a.Triangle b.circle c.rectangle d.cross",
 " 9.How long is an hour in minutes?  a.10 b.100 c.60 d.600",
  "10.What do you call a baby dog? a.foal b.puppy c.piglet d.kitten",
   "11.What language do people from Spain speak? a.German b.French c.English d.Spanish",
  " 12.What date is Christmas Eve?  a.December 23rd b.December 24th c.December 25th d.December 26th",
 " 13.How many jaggy spines does a hedgehog have on average? a.50 b.500 c.1,000 d.5,000",
   "14.What is the 6th letter in the alphabet? a.E b.F c.H d.J"
    ]
Ans=["c","d","a","b","d","c","a","c","c","b","d","b","d","b"]
Money=[0,1000,2000,3000,5000,10000,20000,30000,50000,100000,200000,500000,1000000,5000000,10000000]
for i in range(0,len(Ques)):
    print(Ques[i])
    ans=input("Enter your Answer : ")
    if ans!=Ans[i] :
        print("Sorry!! you won ",Money[i]," Rupees")
        break
    else:
        print("Congratulations!!!!!   You Won ", Money[i+1]," Rupees And your next Question is:")
