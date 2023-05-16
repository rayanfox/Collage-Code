#string functions

emailAddress1 = "kyle@radier.rose.edu"
emailAddress2 = "smith@rose.edu"

if ".rose.edu" in emailAddress1:
    print("accepted")
else:
    print("not accepted")

#slices

myname = "kyle smith"


sep = myname.find(" ")

fname = myname[:sep]
lname = myname[sep:]
print(fname)
print(lname)



     




