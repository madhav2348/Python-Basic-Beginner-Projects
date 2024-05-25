from PyDictionary import PyDictionary


def main():

    #following commented code is basic use of dictionary
#     word_dict ={
#         'hi':'greeting',
#         'eye':'an organ',
#         'earth':'planet'   
#     }

#     while True:
#         word = input("enter word")

#         if word =="":
#             break
#         if word in word_dict:
#             print(word_dict,":",word_dict[word])

    dictionary = PyDictionary()
    
    while True:
        wrd = input("enter word \n")
        if wrd =="":
            break
        print(dictionary.meaning(wrd))
       
