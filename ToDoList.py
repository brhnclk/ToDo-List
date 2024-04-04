import tkinter
import os

class Arayuz:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("To-Do List")
        self.mainWindowGenislik = self.mainWindow.winfo_screenwidth()
        self.mainWindowYukseklik = self.mainWindow.winfo_screenmmheight()
        self.mainWindow.geometry(f"300x450+{(self.mainWindowGenislik//2)-150}+{(self.mainWindowYukseklik//2)}")
        self.top = tkinter.Frame(self.mainWindow)
        self.task = tkinter.Frame(self.mainWindow)
        self.bottom = tkinter.Frame(self.mainWindow)
        self.trash_icon = tkinter.PhotoImage(file='trash.png')
        self.add_icon = tkinter.PhotoImage(file='add.png')
        self.title = tkinter.Label(text='To-Do List')
        self.title.pack()
        self.buton = tkinter.Button(self.task,borderwidth=3,image=self.trash_icon,height=20,width=20,relief='flat',command=self.delCommand)
        self.buton.pack(side='right')
        self.taskBox = tkinter.Listbox(self.task,width=30,height=24,bg='#f0f0f0',relief='flat')
        self.taskBox.bind('<<ListboxSelect>>')
        self.taskBox.pack(side='top',padx=(10, 0),pady=(10, 0))
        taskText = open('tasks.txt','r')
        line = taskText.readline()
        while line != '':
            list(line)
            self.taskBox.insert(tkinter.END,line)
            line = taskText.readline()
        taskText.close()
        self.entryNull = tkinter.StringVar()
        self.entry = tkinter.Entry(self.bottom,width=25,textvariable=self.entryNull)
        self.entry.pack(side='left')
        self.add = tkinter.Button(self.bottom,borderwidth=3,image=self.add_icon,height=20,width=20,relief='flat',command=self.addCommand)
        self.add.pack(side='right')
        self.top.pack(side='top')
        self.task.pack()
        self.bottom.pack(side='bottom')
        tkinter.mainloop()
    def addCommand(self):
        if self.entry.get() != '':
            taskInput = self.entry.get() + '\n'
            addList = open('tasks.txt','a')
            addList.write(taskInput)
            addList.close()
            self.entryNull.set('')
            self.clearBox()
            self.refreshBox()
    def delCommand(self):
        new = open('new.txt','w')
        old = open('tasks.txt','r')
        deleted = self.taskBox.curselection()
        counter = 0
        name = self.taskBox.get(deleted)
        line = old.readline()
        while line != '':
            if line != name:
                new.write(line)
            else:
                if counter != 0:
                    new.write(line)
                counter += 1
            line = old.readline()
        new.close()
        old.close()
        os.remove('tasks.txt')
        os.rename('new.txt','tasks.txt')
        self.clearBox()
        self.refreshBox()
    def refreshBox(self):
        taskText = open('tasks.txt','r')
        line = taskText.readline()
        while line != '':
            self.taskBox.insert(tkinter.END,line)
            line = taskText.readline()
        taskText.close()
    def clearBox(self):
        self.taskBox.delete(0,tkinter.END)
if __name__ == '__main__':
    Arayuz()