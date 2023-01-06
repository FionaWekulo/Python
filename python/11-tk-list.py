import tkinter
from book import Book
import booksSDK
from tkinter import END


tk = tkinter.Tk()
tk.title=("Listbox")
lb = tkinter.Listbox(tk)
lb.pack()


"""

entry=tkinter.Entry(tk)
entry.pack()

lb.insert(0, "hello", "hi", "you")
lb.insert(1, "helo", "i", "you")
lb.insert(END, "h", "i", "y")
lb.delete(0)

"""
"""
def add_to_list():
    lb.insert(END,entry.get ())
    entry.delete(0, END)#IF YOU WANT TO REMOVE VALUE FROM INPUT BOX

def remove_from_list():
    lb.delete(lb.curselection())


entry=tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Add Value", command=add_to_list)
button.pack()


button = tkinter.Button(tk, text="Remove Selected Value", command=remove_from_list)
button.pack()
"""

books = []

def add_to_list():

    if title.get() == "" or pages.get() == "":
        return

    book = Book(title.get(), int(pages.get()))#instance of a book structure
    print(book)
    if(booksSDK.add_book(book)):# adds to database if returns a valid id ith then adds to list
        books.append(book)
        lb.insert(tkinter.END, book)#adds to end of list
    title.delete(0, tkinter.END)#the 2 delete text from input box
    pages.delete(0, tkinter.END)

def delete_from_list():
    index_tuple = lb.curselection()#value selected in list
    if booksSDK.delete_book(books.pop(index_tuple[0])):#if succesfully deleted from db
        lb.delete((index_tuple))#deleting value from list


for book in booksSDK.get_books():#prints all the books currently in database
    books.append(book)#adds on new books added
    lb.insert(tkinter.END, book)


add = tkinter.Button(tk, text="Add Book", command=add_to_list)
add.pack()

delete = tkinter.Button(tk, text="Delete selected Book", command=delete_from_list)
delete.pack()

tkinter.Label(tk, text="Book Title:").pack()
title = tkinter.Entry(tk, text="Title to Add:")
title.pack()

tkinter.Label(tk, text="Number of Pages:").pack()
pages = tkinter.Entry(tk, text="Number of pages:")
pages.pack()

tk.mainloop()
