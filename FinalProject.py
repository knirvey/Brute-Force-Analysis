import hashlib #library used for hashing
import itertools #library used for password generating loop
import string
import time
def readHash(fileStr):
    print("Reading files..")
    fileRead = open(fileStr,'r')
    HashList = [] #create empty list
    for line in fileRead:
        line = line.strip() #read each line and strip the \n
        HashList.append(line) #append the hashes to the list
    fileRead.close()
    return HashList

#returns the given string hashed using md5 hashing
#encode() converts the string(unicode) to bytes for input
#hexdigest() converts the retured binary data to hexadecimal string
def md5Hashing(GenStr):
    return hashlib.md5(GenStr.encode()).hexdigest()

def main():
    HashList = readHash('hashes.txt')
    print(HashList) #print out hashes read from the file(used in debugging process to make sure it's reading correctly)
    count = 0 #letters for generated passwords
    while HashList: #Until system cracks all the hashes from the list
        count+=1 #length of the generated password
        characters = string.ascii_letters + string.digits #letters used in generating passwords, include all ascii letters and digits
        beganTime = time.time() #record the initial time
        for password in itertools.product(characters, repeat=count): #checks all the possible combination(product) of characters for the length of count
            password = ''.join(password) #join the selected letters
            hashedPass = md5Hashing(password) #Hashing the generated password
            if hashedPass in HashList: #if hashed password matched with hashes
                timeDuration = time.time() - beganTime #calculate the time duration
                print("Cracked => " + password + " || Time Required => " + str(round(timeDuration,4)) + "s") #rounding the calculated second for readability
                HashList.remove(hashedPass) #remove the hashes from the list
                beganTime = time.time() #updating the inital time



main()