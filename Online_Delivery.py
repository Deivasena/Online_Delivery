def zip():
	print("\n\n")
	print("***********")
	print("*    WELCOME TO ZIP    *")
	print("***********")
	print("|/|----------------|/|")
	print("| |  1. LOGIN      | |")
	print("|/|----------------|/|")
	print("| |  2. REGISTER   | |")
	print("|/|----------------|/|")
	print("| |  3. EXIT       | |")
	print("|/|----------------|/|")
	ip=input("\nEnter your choice:")
	match ip:
		case "1":
			login1()
		case "2":
			register()
		case "3":
			exit()
		case _:
			print("INVALID CHOICE")
			print("\n Enter your choice again")
			zip()
def ziplogin():
	print("\n\n")
	print("*******************")
	print("*    WELCOME TO ZIP   *")
	print("*******************")
	print("|/|-------------------------|/|")
	print("| |  1. HOTEL LIST  | |")
	print("|/|-----------              |/|")
	print("| |  2. VIEW PROFILE | |")
	print("|/|-------------------------|/|")
	print("| |  3. EXIT         | |")
	print("|/|-------------------------| |")
	ip=input("\nEnter your choice:")
	match ip:
		case "1":
			hotel()
		case "2":
			view(name,loc,no)
		case "3":
			exit()
		case _:
			print("INVALID CHOICE")
			print("\nEnter your choice again")
			ziplogin()
		
def hotel():
	print("\n\n")
	print("****************************")
	print("*     LIST OF HOTEL    *")
	print("****************************")
	print("|/|---------------------|/|")
	print("| |    1. MUTHU MESS    | |")
	print("|/|---------------------|/|")
	print("| |    2. MEAT & EAT    | |")
	print("|/|---------------------|/|")
	print("| |    3. BHUGARI       | |")
	print("|/|---------------------|/|")
	print("| |    4. DELICE        | |")
	print("|/|---------------------|/|")
	print("| |    5. EXIT          | |")
	print("|/|---------------------|/|")
	ip=input("Enter your choice:")
	match ip:
		case "1":
			print("Welcome to MUTHU MESS")
			menu()
		case "2":
			print("Welcome to MEAT & EAT")
			menu()
		case "3":
			print("Welcome to BHUGARI")
			menu()
		case "4":
			print("Welcome to DELICE")
			menu()
		case "5":
			print("Welcome to EXIT")
		case _:
			print("INVALID CHOICE")
			hotel()

def login():
	global name
	name="ADHVIK"
	global loc
	loc="KARAIKAL"
	global no
	no=9994618441
	global user1
	user1="admin"
	global passs
	passs="admin"
	global get
	get=passs
	name1="admin"
	print("\n Please enter your details: ")
	id=input("\n\n\t Username:")
	pass1=input("\n\t Password:")
	if (user1==id) & (passs==pass1):
		print("\n Login Successfull...\n")
		ziplogin()
	else:
		print("\n Login Failed")
	
def login(id1,pass1):
	print("\n Please enter your details:")
	id=input("\n\n\t Username:")
	pass2=input("\n\t Passward:")
	if (id==id1) & (pass1==pass2):
		print("\n Login Successfull...\n")
		ziplogin()
	else:
		print("\n Login Failed")

def register():
	print("\n Please enter your details")
	global name
	name = input("\n Please enter your Name: ")
	global no
	no=input("\n Please enter your Mobile No: ")
	global loc
	loc = input("\n Please enter your Location: ")
	id1=input("\n Create Password:")
	global get
	pass1=get
	print("\n\t Registration Successfull.")
	print("\n\t Please Login...")
	login(id1,pass1)

def view(name,loc,no):
	print("\n\n")
	print("\t************************************")
	print("\t|                                   |")
	print("\t     Name of User  :",name)
	print("\t|                                   |")
	print("\t      Location :",loc)
	print("\t|                                   |")
	print("\t     Mobile Number :",no)
	print("\t|                                   |")
	print("\t************************************")
	print("\n\tPress 1 to back <or> Press 2 to Exit.")
	ip=int(input("Enter your Choice :"))
	if (ip==1):
		ziplogin()
	else:
		exit()
def menu():
	print("\n\n")
	print("**************************************")
	print("*          Menu            *")
	print("**************************************")
	print("|/|-------------------------|/|")
	print("| |   1.MUTTON GRAVY        | |")
	print("|/|-------------------------|/|")
	print("| |   2.MUTTON BRIYANI      | |")
	print("|/|-------------------------|/|")
	print("| |   3.CHICKEN GRAVY       | |")
	print("|/|-------------------------|/|")
	print("| |   4.CHICKEN BRIYANI     | |")
	print("|/|-------------------------|/|")
	print("| |   5.PANEER FRIED RICE   | |")
	print("|/|-------------------------|/|")
	print("| |   6.CHICKEN BUTTER MASALA| |")
	print("|/|-------------------------|/|")
	print("| |   7. EXIT               | |")
	print("|/|-------------------------|/|")
	ip=input("Enter your choice:")
	match ip:
		case "1":
			print("\n\n")
			print("===================")
			print("  | MUTTON GRAVY  |")
			print("===================")
			print("\n  1Qty-Price:",150)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			global f
			f=(150*e)
			print("\n\n Totak cost is ",f)
			pay()
		case "2":
			print("\n\n")
			print("===================")
			print("  | MUTTON BRIYANI |")
			print("===================")
			print("\n 1Qty-Price:",200)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			f=(200*e)
			print("\n\n Total cost is ",f)
			pay()
		case "3":
			print("\n\n")
			print("===================")
			print("  | CHICKEN GRAVY |")
			print("===================")
			print("\n 1Qty-Price:",100)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			f=(100*e)
			print("\n\n Total cost is ",f)
			pay()
		case "4":
			print("\n\n")
			print("===================")
			print("  | CHICKEN BRIYANI |")
			print("===================")
			print("\n 1Qty-Price:",200)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			f=(200*e)
			print("\n\n Total cost is ",f)
			pay()
		case "5":
			print("\n\n")
			print("===================")
			print("  | PANEER FRIED RICE |")
			print("===================")
			print("\n 1Qty-Price:",150)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			f=(150*e)
			print("\n\n Total cost is ",f)
			pay()
		case "6":
			print("\n\n")
			print("===================")
			print("  | CHICKEN BUTTER MASALA |")
			print("===================")
			print("\n 1Qty-Price:",250)
			print("\n\n")
			e=int(input("\n Enter your Quantity:"))
			f=(250*e)
			print("\n\n Total cost is ",f)
			pay()
		case "7":
			hotel()
		case _:
			print("INVALID CHOICE")
def pay():
	print("\t**************************")
	print("\t==========================")
	print("\t|    1.Proceed to payment   |")
	print("\t|-------------------------")
	print("\t|    2. Back               |")
	print("\t==========================")
	ip=input("Enter your choice :")
	match ip:
		case "1":
			password=input("Enter your Password:")
			if (password==get):
				print("\t======================")
				print("\t|    Payment Successfull. |")
				print("\t|---------------------|")
				print("\t| Your order will be Deliver |")
				print("\t|   in 45 minutes.   |")
				print("\t=======================")
				print("\n\n")
			else:
				print("PAssword Wrong")
				print("Payment Failed..")
		case "2":
			menu()

print("\n\n\n\n\n\n")
get=0
zip()