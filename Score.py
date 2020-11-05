score = input("Enter Score: ")
try:
    flscore = float(score)
except:
    print("Error, this score is not between 0.0 and 1.0")
    quit()

if flscore > 1.0:
  print("Error, this score is not between 0.0 and 1.0")
  quit()

elif flscore >= 0.9:
    print("A")
elif flscore >= 0.8:
    print("B")
elif flscore >= 0.7:
    print("C")
elif flscore >= 0.6:
    print("D")
elif flscore >=0.0 :
    print("F")
else:
    print("Error, this score is not between 0.0 and 1.0")
    quit()
