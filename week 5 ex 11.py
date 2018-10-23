password = "changeme"
count=0
while True:
    print("Please enter your password")
    ask = str(input())
    count+=1
    if count > 5:
            print("Access denied, please press enter to exit and contact security to reset your password.")
            break
    if ask == password:
        count-=1
        print("Accepted")
        print("You messed up", count, "times")
        break
