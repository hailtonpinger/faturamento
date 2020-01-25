from tkinter import *


window = Tk()
window.geometry("800x600")
window.title("Gerar faturamento em python usando Tkinter")


usernameVar = StringVar()
passwordVar = StringVar()



def adminLogin():
    titleLabel = Label(window,text="Faturamento em python :", font="Arial 30", fg="red")
    titleLabel.grid(row=0,column=0,columnspan=4,padx=(40),pady=(10))

    loginLabel = Label(window,text="Administrador Login :",font="Arial 30")
    loginLabel.grid(row=1,column=2,padx=(50),columnspan=2 ,pady=10)

    usernameLabel = Label(window,text="Usuário:",font="Arial 14")
    usernameLabel.grid(row=2,column=2,padx=2,pady=5)

    passwordLabel = Label(window,text="Senha:",font="Arial 14")
    passwordLabel.grid(row=3,column=2,padx=2,pady=5)

    usernameEntry = Entry(window,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=3,padx=20,pady=5)

    passwordEntry = Entry(window,textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=20,pady=5)

    loginButton = Button(window,text="Login",width=20,height=2)
    loginButton.grid(row=4,column=2,columnspan=2)

###################################################################################
def mainwindow():
    titleLabel = Label(window,text="Faturamento em python :", font="Arial 30", fg="green")
    titleLabel.grid(row=0,column=1,columnspan=3,pady=(10,0))

    addButton = Button(window,text="Add Itens",width=15,height=2)
    addButton.grid(row=1,column=0,padx=(10,0),pady=(10,0))

    logoutBtn = Button(window,text="Sair",width=15,height=2)
    logoutBtn.grid(row=1,column=4,pady=(10,0))

    

    ItemLabel = Label(window,text="Selecionar Item:")
    ItemLabel.grid(row=2,column=0,padx=(5,0),pady=(10,0))
    

    quantityLabel = Label(window,text="Quantidade:")
    quantityLabel.grid(row=2,column=2,padx=(5,0),pady=(10,0))

    

    buttonBill = Button(window,text="Gerar Nota")
    buttonBill.grid(row=2,column=4,padx=(5,0),pady=(10,0))

    
        

            

mainwindow()
window.mainloop
