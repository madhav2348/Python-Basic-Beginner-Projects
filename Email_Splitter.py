def main():
    print("Email Slicer")
    print("")

    email = input("Enter email")
    (username,domain)= email.split("@")
    (domain,extention)= domain.split(".")

    print("Username",username)
    print("Domain",domain)
    print("Extention",extention)

main()
