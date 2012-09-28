####################
#
# Super Awesome Program Deleter
# by Michael Aboff
# January 2012
#
####################

# Define the server folder here. If left empty, or there is no internet access, the program will look in the directory it lives. Example: "http://www.example.com/superdeleterconfigs/"
server = ""

# Define the file extension the script looks for.
fileExtension = ".sapd"


import os,sys,socket,urllib2, shutil

def deleteFiles(someArray):
    """
    Attempt to remove any directories or files listed in the provided list.
    """
    print("\n")
    for fileHandle in someArray:
        if os.path.isdir(os.path.expanduser(fileHandle.strip())):
            print("Attempting to delete DIRECTORY: "+fileHandle)
            try:
                shutil.rmtree(os.path.expanduser(fileHandle.strip()))
                print("Folder Deleted")
            except:
                print(sys.exc_info()[1])
        else:
            print("Attempting to delete FILE: "+fileHandle)
            try:
                os.remove(os.path.expanduser(fileHandle.strip()))
                print("File Deleted")
            except:
                print(sys.exc_info()[1])
            
def listFilesToDelete(someArray):
    """
    Prints the list of files that will be deleted and waits for user's
    confirmation.
    """
    print("\n")
    print("The following files/directories will be deleted: ")
    for fileHandle in someArray:
        print(fileHandle)
    shouldContinue = ""
    while(shouldContinue == ""):
        shouldContinue = str(raw_input("Continue? (y/n): "))
        if shouldContinue == "y" or shouldContinue == "yes":
            print("Proceeding to remove files/directories...")
            deleteFiles(someArray)
        elif shouldContinue == "n" or shouldContinue == "no":
            print("File deletion cancelled. Terminating program...")
            return
        else:
            shouldContinue = ""
            print("Invalid Choice")
        
def determineConnection():
    """
    Attempts to connect to connect to the config server provided at the 
    top of the file. If not, then the program will look locally for the 
    config file.
    """
    try:
        response = urllib2.urlopen(server,timeout=1)
        print("Connection Established")
        return True
    except:
        print("Connection Failed")
    return False
    
def gatherInternetLists():
    serverHandle = urllib2.urlopen(server)
    return getNamesFromInternetFileNames(parseFileNames(serverHandle))
    
def getNamesFromInternetFileNames(fileNameArray):
    """
    Attempts to parse the list of files provided in a public directory
    on the defined config server.
    """
    dictLists = {}
    for fileName in fileNameArray:
        dictLists[fileName] = []
        fileHandle = urllib2.urlopen(server+"/"+fileName)
        for line in fileHandle:
            dictLists[fileName].append(line)
    return dictLists
            
def parseFileNames(handle):
    fileNames = []
    for line in handle:
        if "a href" in line:
            name = line.split("a href=\"")[1].split("\">")[0].strip()
            if name.endswith(fileExtension):
                fileNames.append(name)
    return fileNames

def getNamesFromFolder():
    dictLists = {}
    for fileName in os.listdir(os.getcwd()):
        if fileName.endswith(fileExtension):
            dictLists[fileName] = []
            fileHandle = open(fileName, "r")
            for line in fileHandle:
                dictLists[fileName].append(line)
    return dictLists
    
def getLists():
    """
    Attempts to get the configuration list from the defined server, if 
    not, then attempts to retrieve list from the current directory.
    """
    print("Attempting to retrieve configuration files...")
    if(determineConnection()):
        dictLists = gatherInternetLists()
        return dictLists
    else:
        return getNamesFromFolder()

def main():
    print("--- Super File Deleter by Michael Aboff ---")
    print("Attempting to establish a connection to %s..." % server)
    dictLists = getLists()
    keyLists = dictLists.keys()
    print("\n")
    print("Available Configuration Files:")
    print("[0] Exit")
    for i in range(1, len(keyLists)+1):
        print("["+str(i)+"] "+keyLists[i-1])
    choice = "-1"
    while(int(choice) not in range(0, len(keyLists)+1)):
        try:
            choice = str(input("Choose a file to use: "))
            choice = int(choice)
            if choice in range(0, len(keyLists)+1):
                if choice == 0:
                    print("Terminating...")
                    return
                else:
                    print("User chose "+keyLists[choice-1])
            else:
                choice = "-1"
                print("Invalid Choice.")
        except:
            choice = "-1"
            print("Invalid Choice.")
    if choice != "-1":
        listFilesToDelete(dictLists[keyLists[choice-1]])
    
    

main()
