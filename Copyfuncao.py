import os
pathquiz=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/quiz/")
pathfuncaoFinal=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/quiz/funcaoquiz.py")
with open(pathfuncaoFinal, "w") as e:
  with open("{}funcaoquiz.txt".format(pathquiz),"r") as abc:
      for lines in abc.readlines():
          e.write(lines)
