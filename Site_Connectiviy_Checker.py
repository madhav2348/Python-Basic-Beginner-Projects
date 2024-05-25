import urllib.request as urllib



def main(url):
    print("checking.... \n")
    response = urllib.urlopen(url)
    print("your response",response.getcode())

    
inturl = input("enter your url")
main(inturl)
