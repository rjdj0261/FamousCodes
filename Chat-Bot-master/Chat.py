try:
    import pyrebase
except:
    import subprocess,sys
    print("This process will happen for first time only\nInstalling pyrebase .....")
    subprocess.call([sys.executable, "-m","pip","--disable-pip-version-chec","-q", "install", 'pyrebase'])
    print("downloaded pyrebase succesfully .....")


#main code
import pyrebase
#incryption and decryption
ch = [123, 34, 97, 112, 105, 75, 101, 121, 34, 58, 32, 34, 65, 73, 122, 97, 83, 121, 68, 85, 53, 107, 50, 117, 88, 66, 86, 105, 89, 98, 82, 111, 55, 50, 98, 82, 72, 56, 103, 54, 82, 105, 68, 78, 80, 54, 109, 95, 117, 83, 111, 34, 44, 34, 97, 117, 116, 104, 68, 111, 109, 97, 105, 110, 34, 58, 32, 34, 112, 121, 114, 101, 98, 97, 115, 101, 116, 117, 116, 111, 114, 105, 97, 108, 46, 102, 105, 114, 101, 98, 97, 115, 101, 97, 112, 112, 46, 99, 111, 109, 34, 44, 34, 100, 97, 116, 97, 98, 97, 115, 101, 85, 82, 76, 34, 58, 32, 34, 104, 116, 116, 112, 115, 58, 47, 47, 112, 121, 114, 101, 98, 97, 115, 101, 116, 117, 116, 111, 114, 105, 97, 108, 46, 102, 105, 114, 101, 98, 97, 115, 101, 105, 111, 46, 99, 111, 109, 34, 44, 34, 112, 114, 111, 106, 101, 99, 116, 73, 100, 34, 58, 32, 34, 112, 121, 114, 101, 98, 97, 115, 101, 116, 117, 116, 111, 114, 105, 97, 108, 34, 44, 34, 115, 116, 111, 114, 97, 103, 101, 66, 117, 99, 107, 101, 116, 34, 58, 32, 34, 112, 121, 114, 101, 98, 97, 115, 101, 116, 117, 116, 111, 114, 105, 97, 108, 46, 97, 112, 112, 115, 112, 111, 116, 46, 99, 111, 109, 34, 44, 34, 109, 101, 115, 115, 97, 103, 105, 110, 103, 83, 101, 110, 100, 101, 114, 73, 100, 34, 58, 32, 34, 55, 51, 48, 57, 48, 55, 54, 51, 57, 54, 57, 52, 34, 44, 34, 97, 112, 112, 73, 100, 34, 58, 32, 34, 49, 58, 55, 51, 48, 57, 48, 55, 54, 51, 57, 54, 57, 52, 58, 119, 101, 98, 58, 54, 102, 50, 54, 102, 51, 102, 55, 101, 52, 54, 100, 50, 53, 102, 49, 49, 100, 54, 101, 100, 102, 34, 44, 34, 109, 101, 97, 115, 117, 114, 101, 109, 101, 110, 116, 73, 100, 34, 58, 32, 34, 71, 45, 78, 70, 84, 51, 81, 53, 75, 57, 90, 55, 34, 125]



lst=[]
for i in ch:
    lst.append(chr(i))
dcod = eval("".join(lst))

#getting key
config = dcod
#initializing app
firebase = pyrebase.initialize_app(config)
#creating object
db = firebase.database()
#getting data for finding length
data_child = db.child("all messages").get()
data_data = data_child.val()
counter = len(data_data)+1

#getting user name and msg
name = input("enter your name : ")
msg = input("enter msg : ")
#passing info to real time data bse
path = db.child("all messages").child("msg"+str(counter))
data = {"Name":name,"Message":msg}
path.set(data)
print("\n\n==========================================\n\n")

#fetching data from object
data_child = db.child("all messages").get()
data_data = data_child.val()
for i in data_data:
    name = data_data[i]["Name"]
    print(name+" :")
    msg = data_data[i]["Message"]
    print(msg)
    print("------------------------------------------")
    print()
