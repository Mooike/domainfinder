from selenium import webdriver




#Get User Input
print("Search for domain")
user_input = input(": ")
#print(user_input)

#open godaddy.com
browser = webdriver.Chrome(executable_path=r"C:\Users\mikel\Downloads\chromedriver_win32 (1)\chromedriver.exe")
request =" https://de.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=" + user_input
browser.get(request)

print="----Look at Chrome----"