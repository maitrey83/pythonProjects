import os
print ("find my repository")
currentPath = os.getcwd()
print(currentPath)
changeToPath = "/Users/Maitrey/Documents/pythonProject"
changePath = os.chdir(changeToPath)
print("After changing Path: ")
print (os.getcwd())


