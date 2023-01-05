class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return True

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    
    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None


########## Passing by Object Reference ##########


book = Book("Where Is My Mother?", 100)
print(book)

def modify(book): #FUNCTIONS CAN CHANGE THE DATA OF OBJECTS
    book.title = "Changed noob"

modify(book)
print(book, end="\n\n")

#What iF we print id to follow? 

def modify(book): 
    print(id(book))
    book.title = "Changed noob"
    print(id(book))

print(id(book))
modify(book)
print(id(book), end="\n\n")#you only modifid the title

#We get the same number for everything

book = Book("Are You My Mother?", 100)
print("let's reassign")
def modify(book): 
    print(id(book))
    book = Book("Changed noob", 100)
    print(id(book)) #This is a different id. 
    #The original is unchanged. Reassigning

print(id(book))#original id as function hasnt been called
modify(book)#calling it give 2 ids one original one for new object
print(id(book))#we continue with original object as don with function
print(book, end="\n\n") #Stayed the same!


########## Reading from a file ##########

file = open("input.txt", "a") #append. Creates if not there
file = open("input.txt", "w") #overwrites
#file = open("input.txt", "r+") #Read and write. Throws exception 
# if not there
#not as easy to work with on r/w in my opinion

#\t to separate title from page count
file.write("Are You My Mother?\t72\n")
file.write("The Digging-est Dog\t72\n")
file.write("Hi")
file.close() #close when done

file = open("input.txt", "r")

#for line in file:
#    print(line, end="") #end="" as \n is kept in line
#print()

#Numerous ways to read into list. Here is one. 
data = file.read().split('\n')
print(data)
#https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

file.close()

#Each line is title\tpages so we split it. 
book1_data = data[0].split('\t')
book = Book(book1_data[0], book1_data[1])

book2_data = data[1].split('\t')
book2 = Book(book2_data[0], book2_data[1])

print(book)
print(book2, end="\n\n")


########## Intro to Exception handling ##########


#When working with files (or doing anything in programming),
#Exceptions can be thrown

#file = open("doesntexist.csv", "r") #get wrecked son

try:
    file=open("inpurte.txt", "r")
except:
    print("File cannot be found", end="\n\n")

try:
    file = open("doesntexist.csv", "r")
except Exception as e:
    print(type(e))
    print(e, end="\n\n")

try:
    file = open("input.txt", "r") #Make sure it exists
    data = int(file.read()) #This should fail
except FileNotFoundError as e: #subclass of OSError
    print("This file is not found")
except OSError as e:
    print("Couldn't open file")
except PermissionError as e:
    print("file is locked")
except ValueError as e:
    print("Cannot parse data. Check file") 
except Exception as e:
    print(type(e))
    print(e)
finally:
    file.close()
    print("Always runs", end="\n\n")


########## with keyword ##########

#shorthand for opening file and automatically closed outside
#  indent
with open("input.txt", "r") as file: #Make sure it exists
    
    try:
        int(file.read())
    except: #example of using thin except here
        print("parse error...etc...")
        #do whatever

print(file.closed, end="\n\n") #closed

#opening can still throw an exception...Maybe do it like so:
try:
    with open("no", "r") as file: 
        int(file.read())
except Exception as e:
    print(e)

#I think this could be written like so but may require another try inside else:   
try:
    file = open('nope')
except OSError as e:
    print(e)
else:
    with file:
        #try:
            file.read()
        #except Exception as e:
        #    print(e)

#https://stackoverflow.com/questions/40640956/python-with-open-except-filenotfounderror/40641103
#https://stackoverflow.com/questions/28633555/how-to-handle-filenotfounderror-when-try-except-ioerror-does-not-catch-it