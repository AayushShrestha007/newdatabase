from tkinter import *
import sqlite3
from tkinter import messagebox

root=Tk()
data= sqlite3.connect("address.db")
c= data.cursor()

# c.execute("""CREATE TABLE address(first_name text,
# last_name text,
# address text,
# city text,
# state text
# zipcode integer)""")
# print("table creted successfully")
def submit():
    data=sqlite3.connect("address.db")
    c=data.cursor()
    c.execute("INSERT INTO address VALUES (:f_name,:l_name,:address,:city,:state)",
    {   'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        
    })

    messagebox.showinfo("address","Inserted successfully")
    data.commit()
    data.close
def query():
    data=sqlite3.connect("address.db")
    c=data.cursor()
    c.execute("SELECT*, oid from address")
    records= c.fetchall()
    print(records)
    print_records=''
    for record in records:
        print_record=str(record[0])+''+str(record[1])+''+'\t'+str(record[5])+'\n'
    query_label=Label(root,text=print_record)
    query_label.grid(row=8,column=0,columnspan=2)
    data.commit()
    data.close()
# def delete():
#     data=sqlite3.connect("address.db")
#     c=data.cursor()
#     c.execute("DELETE FROM address")
#     data.commit()
#     data.close()
def delete():
    data=sqlite3.connect("address.db")
    c=data.cursor()
    c.execute("DELETE from address WHERE oid="+delete_box.get())
    delete_box.delete(0,END)
    data.commit()
    data.close()

def edit():
    global editor
    editor=Toplevel()
    global f_name1
    global l_name1
    global address1
    global city1
    global state1
    
    
    editor.title("update data")
    editor.geometry('800x800')
    data=sqlite3.connect("address.db")
    c=data.cursor()
    record_id=delete_box.get()
    c.execute("SELECT * FROM address WHERE oid=" +record_id)
    records=c.fetchall()
    f_name1=Entry(editor,width=30)
    f_name1.grid(row=1,column=4,padx=20,pady=(10,0))

    l_name1=Entry(editor,width=30)
    l_name1.grid(row=2,column=4,padx=20,pady=(10,0))

    address1=Entry(editor,width=30)
    address1.grid(row=3,column=4,padx=20,pady=(10,0))

    city1=Entry(editor,width=30)
    city1.grid(row=4,column=4,padx=20,pady=(10,0))

    state1=Entry(editor,width=30)
    state1.grid(row=5,column=4,padx=20,pady=(10,0))

    f_name_l=Label(editor,text="Fname")
    f_name_l.grid(row=1,column=0)

    l_name_l=Label(editor,text="lname")
    l_name_l.grid(row=2,column=0)

    addressl=Label(editor,text="address")
    addressl.grid(row=3,column=0)

    cityl=Label(editor,text="city")
    cityl.grid(row=4,column=0)

    statel=Label(editor,text="state")
    statel.grid(row=5,column=0)

    for record in records:
        f_name1.insert(0,record[0])
        l_name1.insert(0,record[1])
        addressl.insert(0,record[2])
        city1.insert(0,record[3])
        state1.insert(0,record[4])
    
    edit_btn= Button(editor,text="Save",command=update)
    edit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=30)
    
    # data.commit()
    # data.close()
def update():
    data=sqlite3.connect('address.db')
    c=data.cursor()
    record_id=delete_box.get()
    c.execute("""UPDATE address SET
    first_name= :first,
    last_name=:last,
    address= :address,
    city=:city,
    state=:state
    WHERE oid= :oid""",
    {'first':f_name1.get(),
      'last':l_name1.get(),
      'address':address1.get(),
      'city':city1.get(),
      'state':state.get(),
      'oid':record_id
    }
    )
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1)
address =Entry(root,width=30)
address.grid(row=2,column=1)
city=Entry(root,width=30)
city.grid(row=3,column=1)
state=Entry(root,width=30)
state.grid(row=4,column=1)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box=Entry(root,width=30)
delete_box.grid(row=6,column=1)

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="l_name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="city")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zip_label=Label(root,text="label")
zip_label.grid(row=5,column=0)

delete_label=Label(root,text="delete")
delete_label.grid(row=6,column=0)

submit_btn= Button(root,text="add record",command=submit)
submit_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10)

query_btn=Button(root,text="Show record", command=query)
query_btn.grid(row=14,column=0,columnspan=2,pady=10,padx=10,ipadx=10)
delete_btn=Button(root,text="Delete",command=delete)
delete_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=10)
update_edit=Button(root,text="Edit",command=edit)
update_edit.grid(row=16,column=0,columnspan=2,pady=10,padx=10,ipadx=30)
root.mainloop()


