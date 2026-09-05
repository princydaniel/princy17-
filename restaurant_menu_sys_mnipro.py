import sqlite3
con=sqlite3.connect('Login.db')
c=con.cursor()


#*************************** USER TABLE ********************************
c.execute("""
              CREATE TABLE IF NOT EXISTS Users(
              ID INTEGER PRIMARY KEY ,
              Username TEXT UNIQUE NOT NULL,
              Password TEXT NOT NULL,
              Role INTEGER NOT NULL
              );
          """)
#**************************** MENU TABLE *********************************
c.execute("""
                CREATE TABLE IF NOT EXISTS Menu(
                item_id	INTEGER	PRIMARY KEY ,
                Food_Name	VARCHAR	 NOT NULL,
                Food_Category	VARCHAR	 NOT NULL,
                Item_Cost	VARCHAR	 NOT NULL,
                Availability  TEXT	NOT NULL
                );

          """)
#**************************************** ORDER ***************************

c.execute(""" CREATE TABLE IF NOT EXISTS Order_item (
              order_id INTEGER PRIMARY KEY ,
              username TEXT,
              total REAL);
          """)

#**************************** ORDER TABLE **********************************
c.execute(""" CREATE TABLE IF NOT EXISTS Orders(
              Orderitem_Id	INTEGER	PRIMARY KEY,
              order_id	INTEGER	NOT NULL,
              item_id	INTEGER	NOT NULL,
              Quantity	INTEGER	NOT NULL,
              Total_Cost INTEGER	NOT NULL,
              FOREIGN KEY(order_id) REFERENCES Order_item(order_id),
              FOREIGN KEY(item_id) REFERENCES Menu(item_id)
              );

              """)

# ***************************************** LOGIN & REGISTRATION ***************************************
def Register():
 print("*************** Restaurant Online Order *****************")
 u =input("Username:")
 p =(input("Password:"))
 r =input("Role:")

 c.execute("""INSERT INTO Users(Username,Password,Role)
             VALUES(?,?,?)
             """,(u,p,r)
          )
 print("User Created Successfully!!!!!")
 con.commit()

def Login():
    u = input("Username:")
    p = input("Password:")
    c.execute("SELECT * FROM Users WHERE Username=? AND Password=?", (u, p))
    role = c.fetchone()
    # print(x)
    if not role:
        print("Username or Password is incorrect")
        return
    elif role:
        print("welcome to Restaurant Online!!!!!", role[1])
        if role[3]=='Owner':
            while True:

                print("\n===========================================================RESTAURANT MENU SYSTEM======================================================")
                print("1.Add Menu")
                print("2.Display Menu")
                print("3.Update Menu")
                print("4.Delete Menu")
                print("5.View Orders")
                print("6.Delete Orders")
                print("7.Logout")
                print("\n------------------")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    add_menu()
                elif ch == 2:
                    display_menu()
                elif ch == 3:
                    update_menu()
                elif ch == 4:
                    delete_menu()
                elif ch == 5:
                    view_orders()
                elif ch == 6:
                    delete_order()
                elif ch == 7:
                    print("Owner Logout")
                    break
                else:
                    print("Enter a valid choice")

        elif role[3]=='Customer':
            while True:
                print("\n===============================CUSTOMER MENU =================================|")
                print("1. View Menu")
                print("2. Search food items")
                print("3. Add to cart")
                print("4. View cart")
                print("5. Place Order")
                print("6. Logout")
                print("\n------------------")
                ch2 = input("\nEnter your choice: ")
                if ch2 == '1':
                    display_menu()
                elif ch2 == '2':
                    search_food()
                elif ch2 == '3':
                    add_cart(cart)
                elif ch2 == '4':
                    view_cart(cart)
                elif ch2 == '5':
                    place_order(u, cart)
                elif ch2 == '6':
                    print("Customer Logout")
                    print("!!!!! Thank you !!!!!")
                    break
                else:
                   print("Please enter a valid choice")



#                                        |************* OWNER **************|



# #********************************************* ADD MENU ******************************************
def add_menu():
    print("\n*************************** ADD MENU *****************************")
    food=input("Enter food name: ")
    category=input("Enter food category: ")
    price=float(input("Enter food item cost: "))
    avail=input("Enter availability: ")

    c.execute("""   INSERT INTO Menu(Food_Name,Food_Category,Item_Cost,Availability)
                        VALUES(?,?,?,?)""",
              (food,category,price,avail))
    print("\nMenu item added successfully!!!!!")

    con.commit()

#******************************************* DISPLAY MENU ***************************************************
def display_menu():
    print("\n|---------------------------------- DISPLAY MENU ---------------------------------|")
    c.execute("SELECT * FROM Menu")
    print("\n==================================RESTAURANT MENU============================================================================================|")
    print(f"{'Item Id':<20}{'Food Name':<40}{'Food Category':<35}{'Item Cost':<35}{'Availability'}")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------|")

    for item in c.fetchall():

        print(f"{item[0]:<20}{item[1]:<40}{item[2]:<35}{item[3]:<35}{item[4]}")

    con.commit()


#***************************************** UPDATE MENU **********************************************
def update_menu():

    display_menu()
    print("\n|-------------------------------- UPDATE MENU ----------------------------------|")
    food_id=input("Enter food id: ")

    c.execute("SELECT * FROM Menu WHERE Item_Id = ?",(food_id,))
    items=c.fetchone()
    if not items :
        print("Food item not found!")
        return


    print("\nWhat do you want to update?")
    print("1. Food Name")
    print("2. Category")
    print("3. Price")
    print("4. Availability")
    print("\n------------------")
    ch1 = int(input("Enter your choice: "))

    if ch1 ==1:

        up_foodname = input("Enter new food name: ")

        c.execute("""UPDATE Menu SET Food_Name= ? WHERE Item_Id= ?""",
                  (up_foodname, food_id))
        print("Food name updated successfully!")

    elif ch1 ==2:

        up_category = input("Enter new food category: ")

        c.execute("""UPDATE Menu SET Food_Category= ? WHERE Item_Id= ?""",
                  (up_category, food_id))
        print("Food category updated successfully!")

    elif ch1 ==3:
        up_price = input("Enter new food price: ")
        c.execute("""UPDATE Menu SET Item_Cost= ? WHERE Item_Id= ?""",
                  (up_price, food_id))
        print("Food Cost updated successfully!")

    elif ch1 ==4:
        up_avail = input("Enter new food availability: ")
        c.execute("""UPDATE Menu SET Availability= ? WHERE Item_Id= ?""",
                  (up_avail, food_id))
        print("Food Availability updated successfully!")
        return
    con.commit()

#************************************** DELETE MENU **********************************************

def delete_menu():

    display_menu()
    print("\n|------------------------------- DELETE MENU ----------------------------------|")
    item_id=input("Enter item id: ")

    c.execute("DELETE FROM Menu WHERE item_id = ?",(item_id,))

    print("Menu item deleted successfully!")
    con.commit()

#************************************** VIEW ORDER *********************************************
def view_orders():
    print("\n*************************** VIEW ORDER *****************************")
    c.execute("SELECT * FROM Orders")

    print(f"{'Orderitem_id':<20}{'Order id':<40}{'Item id':<35}{'Quantity':<35}{'Total Amount'}")
    print("---------------------------------------------------------------------------------------------------------------------------------------------|")
    for order in c.fetchall():
        print(f"{order[0]:<20}{order[1]:<40}{order[2]:<35}{order[3]:<35}{order[4]}")
    con.commit()

#*************************************** DELETE ORDER ********************************************
def delete_order():

    view_orders()
    print("\n------------------------------ DELETE ORDER --------------------------------")
    c.execute("DELETE FROM Orders WHERE Orderitem_Id=?",input("Enter Order id: "))
    print("Order deleted successfully!")
    con.commit()



#                                      ---------------- CUSTOMER ----------------


#************************************************ SEARCH FOOD ***************************************
def search_food():

    display_menu()
    print("\n--------------------------------- SEARCH FOOD ----------------------------------------")
    search_food = input("\nEnter Search Food Name: ")
    c.execute("""
        SELECT * FROM Menu WHERE Food_Name= ?
        """, (search_food,))
    item1=c.fetchall()

    if not  item1:
        print("\nFood not found.")
        return
    for i in item1:
        print(f"{'Item Id':<20}{'Food Name':<40}{'Food Category':<35}{'Item Cost':<35}{'Availability'}")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f"{i[0]:<20}{i[1]:<40}{i[2]:<35}{i[3]:<35}{i[4]:<35}")
        return
    con.commit()

#****************************************** ADD CART *********************************************
cart={}
def add_cart(cart):
    print("\n----------------------------------- ADD CART -----------------------------------")
    display_menu()

    food_id2 = int(input("\nEnter Food Id: "))
    quantity = int(input("\nEnter Quantity: "))


    c.execute("SELECT item_id, Food_Name, Item_Cost FROM Menu WHERE item_id = ?",(food_id2,))
    item2=c.fetchone()

    if not item2 :
        print("\nFood not found.")
        return

    if food_id2 in cart:
        cart[food_id2]["quantity"]+=quantity
    else:
        cart[food_id2]={"Food_Name":item2[1],
                        "Item_Cost":item2[2],
                        "quantity":quantity,
                        }

    print("Food added to cart.")
    con.commit()


#******************************************** VIEW CART *********************************************

def view_cart(cart):
    print("\n============================================ VIEW CART ==========================================")
    if not cart:
        print("\nFood not found.")
        return
    total=0

    print(f"{'ID'}\t{'Food Name':<15}{'Qty':<15}{'Price':<15}{'Total'}")
    print("-----------------------------------------------------------|")

    for food_id2,item in cart.items():
        price = float(item["Item_Cost"])
        quantity = int(item["quantity"])

        item_total = price * quantity
        total += item_total

        print(
            f"{food_id2:}\t"
            f"{item['Food_Name']:10}\t\t"
            f"{'quantity':15}"
            f"₹{price:<15.2f}"
            f"₹{item_total:.2f}"
        )
    print("\n========================================")
    print(f"Total Bill: ₹{total:.2f}")
    return total


#*********************************************** PLACE ORDER ****************************************


def place_order(u, cart):
    print("\n----------------------------------- PLACE ORDER -----------------------------------")
    if not cart:
        print("Cart is empty.")
        return

    total = view_cart(cart)

    confirm = input("\nPlace order? (yes/no): ")

    if confirm.lower() != "yes":
        print("Order cancelled.")
        return

    # # Insert order
    c.execute("""
                     INSERT INTO Order_item(username, total)
                     VALUES (?, ?)
                """, (u, total))

    order_id = c.lastrowid

    # Insert order items
    for item_id, item in cart.items():

        c.execute("""
        INSERT INTO Orders(Order_id, item_id, quantity,Total_Cost)
        VALUES (?, ?, ?, ?)
        """, (order_id,item_id,item["quantity"],total)
        )

    con.commit()

    print("\nOrder placed successfully!")

    print(f"Total Amount: ₹{total:.2f}")
    print("\nThank you!!!! Come Again !!!")
    cart.clear()

#****************************************** Main Program ***************************************
while True:
    print("************************* Restaurant Sign in ***************************")
    print("1. Login")
    print("2. Register User")
    print("3. Exit")
    print("\n------------------")
    ch=int(input("Enter your choice:"))

    if ch==1:
        Login()


    elif ch==2:
        Register()


    elif ch ==3:

        print("Thank you!")
        break

    else:
        print("Invalid choice")
