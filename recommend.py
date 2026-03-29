import random


Question = ["what are you in the mood for  ?" , "whate genre ?", "how many episodes ?" , "what genre ?" ]
#%% 
def  userInfo():
  for idx ,q in enumerate(Question):
    print(f"{idx+1} {q}\n")
    useranswer = input("=>>").lower()

userInfo()    