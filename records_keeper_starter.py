print("BUSINESS RECORD KEEPER")
import pandas as pd
import datetime
import time

initial_time =time.time()
init_date = datetime.datetime.now()
day =init_date.strftime("%d ")
month =init_date.strftime("%B")
year =init_date.strftime("%Y")

code_list =[]
name_list = []
amount_list = []
source_list = []
#inputing data from source message 
while True:
    code= input("Enter code: ")
    name = input("Enter Name: ")
    source= input("Enter Source: ")
    while True:
        try:
            amount = int(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid Input For Amount.\n Please Enter a Valid Amount.")
    code_list.append(code)
    name_list.append(name)
    amount_list.append(amount)
    source_list.append(source)
    time_lapse =time.time()-initial_time
    if time_lapse>(24*3600):#24 hours
        break
data = {
    "CODE" :(i for i in (code_list)),
    "NAME":(i for i in (name_list)) ,
    "AMOUNT":(i for i in (amount_list)) ,
    "SOURCE":(i for i in (source_list))
}
df = pd.DataFrame(data)
csv_data = df.to_csv( "Day_data",index=False, sep=("\t"))
print("Records of: ",day,month,year,"\n",csv_data)