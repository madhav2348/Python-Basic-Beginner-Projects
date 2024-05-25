quiz = { "1":
         {"ques":"1+1","ans":"2"},
         "2":
         {"ques":"1+2","ans":"3"},
         "3":
         {"ques":"1+3","ans":"4"},
         "4":
         {"ques":"1+4","ans":"5"}
         }


score = 0
for key,value in quiz.items():
     
    print(value["ques"])
    ans = input("ans?")

    if(ans.lower() or ans.upper() == value['ans'].lower() or value['ans'].upper()):
         print("corecct")
         score =+ 1
         print("score earn ",str(score))
    else:
        print("wrong")
        print("coreect ans was",+ value['ans'])
        print("score earn ",str(score))

print("total score ==",score)
