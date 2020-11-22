# Percentage calculator for KERALA state board exams (SSLC/HSE)


print(" Percentage calculator for KERALA state board exams (SSLC/HSE)")
print(" CHOOSE THE BOARD OF THE EXAM  ")
num = int(input(" 1. HSE / 2. SSLC "))
if num == 1 :
    mark = int(input("Enter the marks you scored = "))
    total = int(input("Enter the total marks = "))
    per = (mark/total)*100
    print(f"You have scored {per} percent")
elif num == 2 :
    num_ap = int(input("Enter the number of A+ = "))
    num_a = int(input("Enter the number of A = "))
    num_bp = int(input("Enter the number of B+ = "))
    num_b = int(input("Enter the number of B = "))
    num_cp = int(input("Enter the number of C+ = "))
    num_c = int(input("Enter the number of C = "))
    num_dp = int(input("Enter the number of D+ = "))
    num_d = int(input("Enter the number of D = "))
    per = ((num_ap*9)+(num_a*8)+(num_bp*7)+(num_b*6)+(num_cp*5)+(num_c*4)+(num_dp*3)+(num_d*2))
    print(f"You have scored {per} percent")

else:
    print("INVALID SYNTAX ")
