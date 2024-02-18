from tkinter import *
#Blank function is used to create a feel of using an interactive application as no new window generation is observed whenever a command is used.
def blank():
    blank_label=Label(window,bg="#E0EBE3",width=400,height=400)
    blank_label.place(x=0,y=90)
#New function is used to create entry boxes for name and number of a contact and a save button.
#When the save button is clicked the contact will be saved.
def new():
    blank()
    global name
    global num
    enter_details_label=Label(window,text="ENTER DETAILS",font=("arial",20),bg="#E0EBE3")
    enter_details_label.place(x=100,y=150)

    name_label=Label(window,text='NAME      :',bg="#E0EBE3")
    name_label.place(x=80,y=200)
    name=Entry(window,font=('Arial',12),fg='black',bg='light grey')
    name.place(x=150,y=200)

    num_label=Label(window,text='NUMBER :',bg="#E0EBE3")
    num_label.place(x=80,y=250)
    num=Entry(window,font=('Arial',12),fg='black',bg='light grey')
    num.place(x=150,y=250)
#Appropriate text will be displayed whenever a contact is saved.
    def save():
        global contact_name
        global contact_num
        contact_name=name.get()
        contact_num=num.get()

        if contact_num.isdigit():
            if contact_name and contact_num:
                for contact in data:
                    if contact["name"]==contact_name:
                        dual_label =Label(window, text="Contact already exists. Use other name.",bg='#E0EBE3',font=('garamond',16))
                        dual_label.place(x=30,y=150)
                        return
                data.append({"name": contact_name, "num": contact_num})

                saved_label=Label(window,text="CONTACT SAVED",font=("garamond",20),fg="#043600",bg="#E0EBE3",width=25)
                saved_label.place(x=15,y=150)
        elif not contact_num.isdigit():
            invalid_label = Label(window, text="INVALID NUMBER",font=("garamond",20),fg="red",bg="#E0EBE3",width=25)
            invalid_label.place(x=10, y=150)
        else:
            less_info=Label(window,text="INSUFFICIENT DATA",font=("garamond",20),fg="red",bg="#E0EBE3",width=25)
            less_info.place(x=10,y=150)

    save_button=Button(window,text="SAVE",command=save,height=1,width=10)
    save_button.place(x=80,y=275)
#Search function is used to create a entry box and an enter button.
def search():
    blank()
    global search_name
    search_name=Entry(window,font=("Arial",12),fg="black",bg="light grey")
    search_name.place(x=100,y=200)
    
    enter_button=Button(window,text="ENTER",command=enter,width=10,height=1)
    enter_button.place(x=285,y=195)
#Enter button displays appropriate text and shows whether a contact is in your contacts or not.
#If contact is present number will be displayed or else appropriate text is displayed. 
def enter():
    search_term=search_name.get()
    if search_term:
        for contact in data:
            if contact["name"].lower() == search_term.lower():
                result_label =Label(window, text=f"Number: {contact['num']}",bg='#E0EBE3',font=('roboto',12),width=30)
                result_label.place(x=0,y=225)
                return
        result_label = Label(window, text="CONTACT NOT FOUND",bg='#E0EBE3',font=('roboto',12))
        result_label.place(x=100,y=225)
    else:
        result_label = Label(window, text="No Name Entered",bg='#E0EBE3',font=('roboto',12),width=40)
        result_label.place(x=10,y=225)
#Delete function is used to create a entry box and an enter button.
def delete():
    blank()
    global del_name
    del_name=Entry(window,font=("Arial",12),fg="black",bg="light grey")
    del_name.place(x=100,y=200)
    
    del_enter_button=Button(window,text="ENTER",command=del_enter,width=10,height=1)
    del_enter_button.place(x=285,y=195)
#Del_enter function deletes the contact if it is present in your contacts or else appropriate text is displayed.
def del_enter():
    del_term=del_name.get()
    if del_term:
        for contact in data:
            if contact["name"].lower() == del_term.lower():
                data.remove({"name":contact_name,"num":contact_num})
                del_label =Label(window, text="CONTACT DELETED",bg='#E0EBE3',font=('roboto',12),width=20)
                del_label.place(x=100,y=225)
                return
        del_label = Label(window, text="CONTACT NOT FOUND",bg='#E0EBE3',font=('roboto',12))
        del_label.place(x=100,y=225)
    else:
        del_label = Label(window, text="No Name Entered",bg='#E0EBE3',font=('roboto',12),width=40)
        del_label.place(x=10,y=225)
#Display function is used to display names of all contacts you have in your contact book.
#Total number of contacts will also be displayed in the bottom.
def display():
    blank()
    contacts_text = ""
    for contact in data:
        contacts_text += f"{contact['name']}\n"
    
    my_contacts=Label(window,text="MY CONTACTS",bg="#E0EBE3",font=('garamond',12),fg='dark red')
    my_contacts.place(x=30,y=90)

    contacts=Label(window,text=contacts_text,bg="#E0EBE3",font=('roboto',12))
    contacts.place(x=0,y=110)

    total_label=Label(window, text=f"Total Contacts: {len(data)}",font=("garamond",18),bg="#E0EBE3")
    total_label.place(y=570,x=110)

window=Tk()
window.title('MY CONTACT BOOK',)
label=Label(text='MY CONTACT BOOK',font=('garamond',25),bg='#E0EBE3',fg='#120312',relief=SOLID,borderwidth=1)
label.place(x=40,y=0)
#Window size is configured to only one dimension and can't be maximized or resized for giving an actual feeling of an application.
window.minsize(400,600)
window.config(background="#E0EBE3")
window.resizable(False,False)

search_name=Entry(window,font=("Arial",12),fg="black",bg="light grey")
search_name.place(x=100,y=200)
#Data is the list in which contacts will be saved.
data=[]
#All major command buttons are placed in such a way that they can be accessed whenever needed.
search_button=Button(window,text='SEARCH',command=search,height=1,width=10)
search_button.place(x=200,y=65)
display_button=Button(window,text='DISPLAY',command=display,height=1,width=10)
display_button.place(x=40,y=65)
new_button=Button(window,text="NEW",command=new,height=1,width=10)
new_button.place(x=120,y=65)
enter_button=Button(window,text="ENTER",command=enter,width=10,height=1)
enter_button.place(x=285,y=195)
del_button=Button(window,text="DELETE",command=delete,width=10,height=1)
del_button.place(x=280,y=65)

window.mainloop()
