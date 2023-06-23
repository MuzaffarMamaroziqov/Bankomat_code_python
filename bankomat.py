# with open ("output.txt","w") as f:
#     word=f.write('muzaffar')
#     print(word)

# print("Mamaroziqov Muzaffar", file=open("output.txt","r"))
# print("Mamaroziqov Muzaffar",file=open("output.txt","r"))

# with open("output.txt","a")as f:
#     f.write("\nJamoamizga xush kelibsiz qadirli mehmon!")



# with open("output.txt","r") as f:
#      print(f.read().split())
# print("Assalom aleykum dear my friend", file=open("output.txt","w"))
#
#
# with open("output.txt","r") as f:
#      l=f.read().split()
#      print(l)
#      l[-1]="uncle"
#      print(l)
#      print(*l,file=open("output.txt","w"))
# with open("output.txt")as r:
#      soni=r.read().split("\n")
#      # print(soni)
#      # print(len(soni))
# l=[]
# for i in soni:
#      print(i)
# print(soni,file=open("output.txt","w"))
# with open("output.txt","w") as f:
#      f.write("Cash saccessfully cleared")


from random import randint

class Bankomat:

     def __init__(self,card_number,balance, pincode):
          self.card_number=card_number
          self.balance=balance
          self.pincode=pincode
     def withdraw(self,summa):
          if self.balance >=summa:
             self.balance-=summa
             with open("output.txt", "a") as a:
                  a.writelines(f" {self.card_number}  {self.balance} {self.pincode}\n")
             print(f"{summa} so'm pul muaffaqiyatli yechildi\n")
          else:
               print("Kartada pul yetartli emas\n")


     def append_money(self,new_summa):
          n=randint(0,1)
          if n==1:
               self.balance+=new_summa
               with open("output.txt", "a") as a:
                    a.writelines(f" {self.card_number}  {self.balance} {self.pincode}\n")
               print("Pulingizni kartaga tushurdik!\n")
          else:
               print("Pulingizni qabul qilolmaymiz uzur\n")

     def set_pincode(self,new_pin):
          self.pincode=new_pin
          with open("output.txt", "a") as a:
               a.writelines(f" {self.card_number}  {self.balance} {self.pincode}\n")

          print("Yangi pincode almashtirildi\n")

     def know_balance(self):
          print(f" Sizning xisobingiz : {self.balance}\n")


number=int(input('Karta raqamini kiriting : '))

balance=int(input("Kartangizni balansini kiriting : "))

pin=int(input("Kartangizni pincode ni kiriting :"))

obj1=Bankomat(card_number=number, pincode=pin, balance=balance)



option=12
sorash=0
while option:
     if sorash==0:
      print("Quydagilardan birini tanlang:")
     else:
          print("Yana boshqa amal bajarasizmi ?")
     sorash+=1
     option=int(input(" 1.Pul yechish\n 2.Kartaga pul to'ldirish\n 3.Pincode ni almashtirish\n 4.Balansni ko'rish\n 0.Chiqish\n" ))
     if option==1:
          obj1.withdraw(int(input("Qancha pul yechmoqchisiz : ")))
     elif option==2:
          obj1.append_money(int(input("Qancha pul solishizni kiriting: ")))
     elif option==3:
          obj1.set_pincode(int(input("Yangi pincode ni kiriting : ")))
     elif option==4:
          obj1.know_balance()





