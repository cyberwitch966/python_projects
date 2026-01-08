#This tool will defang an ip address 
#Prompt user to choose between defanging an ip or url 
start = input("Do you want to defang an ip or url? (I/U): ")

#When a user decides to defang an ip address
if start == "I":
    ip = input("Enter the ip address: ") #prompt to enter the ip address
    if ip.isalpha():     #Validates inpurt, preventing a user from entering letters instead of ip address
        print("Invalid input. Enter a valid ip address") 
    #If user inputs a valid ip address they defanging process starts
    #The replace function is used to defang
    else:
         defanged_ip = ip.replace(".", "[.]")
         defanged_ip = defanged_ip.replace("/", "[/]")
         print(f"Normal: {ip}") 
         print(f"Defanged: {defanged_ip}")     
#When a user wants to defang a url. Will not show if user selected I
elif start == "U":
    url = input("Enter the url: ") 
    #iterates through common symbols to get the end result
    defanged_url = url.replace(".", "[.]")
    defanged_url = defanged_url.replace("://", "[://]")
    defanged_url = defanged_url.replace("http", "hxxp")
    defanged_url = defanged_url.replace("ftp", "fxp")
    print(f"Normal: {url}")
    print(f"Defanged: {defanged_url}") 
#If user types anything other than I or U when asked if they want to defang an ip or url
else:

    print("Invalid choice, pick I/U: ")

