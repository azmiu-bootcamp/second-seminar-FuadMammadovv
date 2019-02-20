

sayi=input("bir sayi giriniz: ")
 
rakamlar= {"1":"Bir","2":"İki","3":"Uç","4":"Dord","5":"Bes",
           "6":"Alti","7":"Yeddi","8":"Səkkiz","9":"Doqquz"}
           
onlar=["On","Yirmi","Otuz","Qirx","Elli","Altmis","Yetmis","Seksen","Doxsan"]
 
sayicumlesi=" " 

birlerbasamagi=0 
 
sayac=0 
for i in range(len(sayi)):
    if(len(sayi)==2):
        if(sayac<=1):     
            if((int(sayi[1])!=0)or(i!=1)):
                if((int(sayi[1])!=1)or(i!=1)):
                	
                    sayicumlesi+= rakamlar[sayi[i]]+" "
            sayac=sayac+1
        else:
            if birlerbasamagi==0:  
                if(int(sayi[2])!=0):
                    sayicumlesi+= onlar[int(sayi[i])-1]+" "
                birlerbasamagi=1
            else:
                if(int(sayi[3])!=0):
                    sayicumlesi+= rakamlar[str(sayi[i])]
 
print(sayicumlesi)
