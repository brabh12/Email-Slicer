while True:
#print orders
         print("please enter your id : ")
         email = input().strip()
#---------
         if email.find("@") != -1:
            #username value
            username = email[:email.index("@")]
            #domain value
            domain = email[email.index("@") +1:]
            print("your username is ", username)
            print("your domaine is: ",domain)
         else:
           print("please enter a correct email id")
#---------by rabah.bct
           