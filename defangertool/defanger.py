#This tool will defang an ip address 
#Prompt user to choose between defanging an ip or url 
start = input("Do you want to defang an ip or url? (I/U): ")

#When a user decides to defang an ip address
if start == "I":
    ip = input("Enter the ip address: ")
    if ip.isalpha():
        print("Invalid input. Enter a valid ip address")
    else:
         defanged_ip = ip.replace(".", "[.]")
         defanged_ip = defanged_ip.replace("/", "[/]")
         print(f"Normal: {ip}") 
         print(f"Defanged: {defanged_ip}")                           
elif start == "U":
    url = input("Enter the url: ")
    defanged_url = url.replace(".", "[.]")
    defanged_url = defanged_url.replace("://", "[://]")
    defanged_url = defanged_url.replace("http", "hxxp")
    defanged_url = defanged_url.replace("ftp", "fxp")
    print(f"Normal: {url}")
    print(f"Defanged: {defanged_url}") 
#defanged_url = ip.replace(".", "[.]") 
else:
    print("Invalid choice, pick I/U: ")