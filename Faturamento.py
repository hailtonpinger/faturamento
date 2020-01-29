from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("800x600")
window.title("Faturamento em python usando Tkinter")

usernameVar = StringVar()
passwordVar = StringVar()


options=["Banana","Arroz","Feijao","Acucar","Café","Farinha de trigo"]
itemVariable = StringVar()
itemVariable.set(options[0])
quantityVar = StringVar()

itemRate = 1
rateVar = StringVar()
rateVar.set("%.2f"%itemRate)
costVar = StringVar()


addItemNameVar = StringVar()
addItemTypeVar = StringVar()
addItemRareVar = StringVar()
addItemStoreVar = StringVar()

billsTV = ttk.Treeview(height=15,columns=('Nome Produto','Quantidade','Valor'))


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


def mainwindow():
    window.geometry("830x600")
    titleLabel = Label(window,text="Faturamento em python :", font="Arial 30", fg="green")
    titleLabel.grid(row=0,column=1,columnspan=3,pady=(10,0))

    addButton = Button(window,text="Add Itens:",width=15,height=2,font="Arial 9")
    addButton.grid(row=1,column=0,padx=(10,0),pady=(10,0))

    logoutBtn = Button(window,text="Sair",width=15,height=2,font="Arial 9")
    logoutBtn.grid(row=1,column=4,pady=(10,0))

    
    ItemLabel = Label(window,text="Selecionar Item:",font="Arial 9")
    ItemLabel.grid(row=2,column=0,padx=(5,0),pady=(10,0))

    itemDropDown=OptionMenu(window,itemVariable,*options)
    itemDropDown.grid(row=2,column=1,padx=(5,0),pady=(10,0))



    rateLabel = Label(window,text="Taxa:", font="Arial 9")
    rateLabel.grid(row=1,column=2,padx=(10,0),pady=(10,0))


    rateValue = Label(window,textvariable=rateVar, font="Arial 9")
    rateValue.grid(row=1,column=3,padx=(10,0),pady=(10,0))
    


    costLabel = Label(window,text="Preço:", font="Arial 9")
    costLabel.grid(row=3,column=2,padx=(10,0),pady=(10,0))

    costEntry = Entry(window,textvariable=costVar)
    costEntry.grid(row=3,column=3,padx=(10,0),pady=(10,0))

    
   
    
    quantityLabel = Label(window,text="Quantidade:", font="Arial 9")
    quantityLabel.grid(row=2,column=2,padx=(5,0),pady=(10,0))

    quantityEntry = Entry(window,textvariable=quantityVar)
    quantityEntry.grid(row=2,column=3,padx=(5,0),pady=(10,0))

    buttonBill = Button(window,text="Gerar Nota:", font="Arial 8")
    buttonBill.grid(row=2,column=4,padx=(5,0),pady=(10,0))

                                
    billLabel = Label(window,text="Lista de Produtos:", font="Arial 25")
    billLabel.grid(row=4,column=2)

    billsTV.grid(row=5,column=0, columnspan=5,padx=(10))

    scrollBar = Scrollbar(window,orient="vertical",command=billsTV.yview)
    scrollBar.grid(row=5,column=4,sticky="NSE")


    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0', text="Nome Produto")
    billsTV.heading('#1', text="Taxa")
    billsTV.heading('#2', text="Quantidade")
    billsTV.heading('#3', text="Valor")

  

def addItem():
    window.geometry("900x600")
    
    titleLabel = Label(window,text="Faturamento em python :",width=40,font="Arial 30", fg="forestgreen")
    titleLabel.grid(row=0,column=1,columnspan=5,pady=(10,0))

    itemNameLabel = Label(window,text="Nome :",font="Arial 9")
    itemNameLabel.grid(row=1,column=1,pady=(10,0))

    itemNameEntry = Entry(window,textvariable=addItemNameVar)
    itemNameEntry.grid(row=1,column=2,pady=(10,0))

    
    itemRateLabel = Label(window,text="Taxa Produto:",font="Arial 9")
    itemRateLabel.grid(row=1,column=3,pady=(10,0))

    itemRateEntry = Entry(window,textvariable=addItemTypeVar)
    itemRateEntry.grid(row=1,column=4,pady=(10,0))


    itemTypeLabel = Label(window,text="Tipo Produto:",font="Arial 9")
    itemTypeLabel.grid(row=2,column=2,pady=(10,0))

    itemTypeEntry = Entry(window,textvariable=addItemRareVar)
    itemTypeEntry.grid(row=2,column=2,pady=(10,0))



    storeTypeLabel = Label(window,text="Tipo Armazenamento:",font="Arial 9")
    storeTypeLabel.grid(row=2,column=3,pady=(10,0))

    storeEntry = Entry(window,textvariable=addItemStoreVar)
    storeEntry.grid(row=2,column=4,pady=(10,0))
    

    AddItemButton = Button(window,text="Adicionar Item:",width=20,height=2,font="Arial 9")
    AddItemButton.grid(row=3,column=3,pady=(10,0))


mainwindow()
window.mainloop
