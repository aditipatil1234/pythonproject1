print("\n" * 5)                  

import datetime                    
import os       
from fpdf import FPDF                   

list_parts = []                    
list_oparts = []                   
list_services = []                 

list_item_price = [0] * 100        
                                  
var_discount_1 = 200                      
var_discount_2 = 1000                     
var_discount_3 = 5000                     
var_discount_1_rate = 0.05                
var_discount_2_rate = 0.10                
var_discount_3_rate = 0.15                


navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 


def def_default():
    global list_oparts, list_parts, list_services, list_item_services, list_item_price     
    list_item_services = [0] * 100                    
def_default()                                      
                                                   


def def_main():
    while True:
        print("*" * 28 + "GARAGE MANAGEMENT SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(S) SERVICES\n"                              
              "\t(R) REPORT\n"
              "\t(P) PAYMENT\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'S'):                                          
                print("\n" * 10)                                        
                def_SERVICES_menu()                                          
                break                                                     
            elif (input_1 == 'R'):                                        
                print("\n" * 10)                                        
                def_report()                                              
                break                                                     
            elif (input_1 == 'P'):                                        
                print("\n" * 10)                                         
                def_payment()                                             
                break                                                     
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")        

def def_SERVICES_menu():                                                                               
    while True:                                             
        print("*" * 31 + "SERVICES PAGE" + "*" * 31 + "\n"    
              "\t(P) SPARE PARTS\n"
              "\t(O) OTHER SERVICES\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'P'):  
                print("\n" * 10)
                def_parts_oparts_services()
                break
            elif (input_1 == 'O'):
                print("\n" * 10)
                def_other_services() 
                break
            elif (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!") 
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_full_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_parts.fsd', 'r') 
    for i in file_foods: 
        list_parts.append(str(i.strip())) 
    file_foods.close()

    

    file_services = open('files'+navigator_symbol+'list_services.fsd', 'r') 
    for i in file_services:
        list_services.append(str(i.strip()))
    file_services.close()

    i = 0
    while i <= (len(list_parts) - 1): 
        if 'Rs' in list_parts[i]:
            list_parts[i] = str(list_parts[i][:list_parts[i].index('Rs') - 1]) + ' ' * (20 - (list_parts[i].index('Rs') - 1)) + str(list_parts[i][list_parts[i].index('Rs'):])
        i += 1

    i = 0
    while i <= (len(list_oparts) - 1):
        if 'Rs' in list_oparts[i]:
            list_oparts[i] = str(list_oparts[i][:list_oparts[i].index('Rs') - 1]) + ' ' * (20 - (list_oparts[i].index('Rs') - 1)) + str(list_oparts[i][list_oparts[i].index('Rs'):])
        i += 1

    i = 0
    while i <= (len(list_services) - 1):
        if 'Rs' in list_services[i]:
            list_services[i] = str(list_services[i][:list_services[i].index('Rs') - 1]) + ' ' * (20 - (list_services[i].index('Rs') - 1)) + str(list_services[i][list_services[i].index('Rs'):])
        i += 1
def_full_file_reader()

def def_file_sorter(): 
    global list_parts, list_oparts, list_services
    list_parts = sorted(list_parts)
    list_oparts = sorted(list_oparts)
    list_services = sorted(list_services)

    i = 0
    while i < len(list_parts):
        list_item_price[i] = float(list_parts[i][int(list_parts[i].index("Rs") + 2):]) 
        i += 1

    i = 0
    while i < len(list_oparts):
        list_item_price[40 + i] = float(list_oparts[i][int(list_oparts[i].index("Rs") + 2):]) 
        i += 1

    i = 0
    while i < len(list_services):
        list_item_price[80 + i] = float(list_services[i][int(list_services[i].index("Rs") + 2):]) 
        i += 1
def_file_sorter()

def def_parts_oparts_services():
    while True:
            print("*" * 26 + "SPARE PART NAMES" + "*" * 26)
            print(" |NO| |PART NAME|        |PRICE|  |  |NO| |PART NAME|        |PRICE|")

            i = 0
            while i < len(list_parts) or i < len(list_oparts):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_parts):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_parts[i]) + "  | " 
                else:
                    food = " " * 36 + "| " 
                if i < len(list_oparts):
                    drink = "(" + str(41 + i) + ")" + " " + str(list_oparts[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

            input_1 = input("Please Select Your Operation: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 10)
                def_main() 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_parts) and int(input_1) > 0) or (int(input_1) <= len(list_oparts) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_parts[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(list_oparts[int(input_1) - 41])) 
                     except:
                        pass

                     input_2 = input("How Many Parts You Want?: ").upper() 
                     if int(input_2) > 0:
                        list_item_services[int(input_1) - 1] += int(input_2) 
                        print("\n" * 10)
                        print("Successfully placed!")
                        def_parts_oparts_SERVICES() 
                        break
                     else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_other_services():
    while True:
        print("*" * 29 + "OTHER SERVICES" + "*" * 29)
        print(" |NO| |SERVICE NAME|            |PRICE|")  

        i = 0
        while i < len(list_services):
            print(" (" + str(81+ i) + ")" + " " + str(list_services[i])) 

            i += 1

        print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)

        input_1 = input("Please Select Your Operation: ").upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        if (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        if (input_1 == 'P'):
            print("\n" * 10)
            def_payment() 
            break
        try:
            int(input_1)
            if (int(input_1) > 80) and (int(input_1) < 100):
                print("\n" * 10)
                print("Successfully placed: " + str(list_services[int(input_1) - 81])) 
                list_item_SERVICES[int(input_1) - 1] = 1
                def_other_services()
                break
            else:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")
        except:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_report():
    while True:
        print("*" * 33 + "REPORT" + "*" * 33 + "\n")
        file_report = open('files'+navigator_symbol+'report.fsd', 'r').read() 
        print(file_report)
        print("\n(M) MAIN MENU          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        elif (input_1 == 'E'):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n") 
            break
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def def_payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(list_item_services): 
            if(list_item_services[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(list_parts[i]) + "  x  " + str(list_item_services[i]) 
                    print(" " * 17 + str(list_parts[i]) + "  x  " + str(list_item_services[i])) 
                    total_price += list_item_price[i] * list_item_services[i] 
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(list_oparts[i - 40]) + "  x  " + str(list_item_services[i])
                    print(" " * 17 + str(list_oparts[i - 40]) + "   x  " + str(list_item_services[i]))
                    total_price += list_item_price[i] * list_item_services[i] 
                if (i >= 80) and (i < 100):
                    report_new += "\n" + " " * 17 + str(list_services[i - 80])
                    print(" " * 17 + str(list_services[i - 80]))
                    total_price += list_item_price[i] * list_item_services[i] 
                i += 1
            else:
                i += 1
        
        
        
        if total_price > var_discount_3: 
            total_price -= total_price * var_discount_3_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_3_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_3_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
                
            
        elif total_price > var_discount_2: 
            total_price -= total_price * var_discount_2_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_2_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_2_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
                
            
        elif total_price > var_discount_1: 
            total_price -= total_price * var_discount_1_rate 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT RATES:      % " + str(var_discount_1_rate * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   Rs " + str(round(total_price * var_discount_1_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
                
            
        else:
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       Rs " + str(round(total_price, 2)))
        
        temp = report_new
        f = open("Receipt.txt",'w')
        f.write(report_new)
        f.close()
        print("\n (P) PAY           (M) MAIN MENU           (R) REPORT           (PR) Print          (E) EXIT\n" + "_" * 72)
        input_1 = str(input("Please Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)
            print("Successfully Paid!")
            file_report = open('files'+navigator_symbol+'report.fsd', 'a') 
            file_report.write(report_new)
            file_report.close()
            def_default() 
        elif (input_1 == 'M'):
            print("\n" * 10)
            def_main() 
            break
        elif (input_1 == 'R'):
            print("\n" * 10)
            def_report() 
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU" + "*" * 31 + "\n")
            break
        elif ('PR' in input_1):


            f = open("Receipt.txt",'w')
            f.write(temp)
            f.close()
            
            pdf = FPDF()   
   
            # Add a page
            pdf.add_page()
               
            # set style and size of font 
            # that you want in the pdf
            pdf.set_font("Arial", size = 15)
            
            # open the text file in read mode
            f = open("Receipt.txt", "r")
              
            # insert the texts in pdf
            for x in f:
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
               
            # save the pdf with name .pdf
            pdf.output("Receipt.pdf")   
            print("Bill Created. ")
        else:
            print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")

def_main() 
