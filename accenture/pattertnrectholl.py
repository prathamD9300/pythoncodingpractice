# for i in range(6):
#     for j in range(5):
#         if i ==0 or j ==0 or i == 5 or j == 4:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
# for i in range(0,4):
    
#     for j in range(0,4-i-1):
#         print(" ",end='')
#     for k in range(6):
#         print("*",end='')
#     print()
# num = int(input("Enter the Number: "))
# num = 4
# for i in range(0, num):
#     for j in range(0, num-i-1):
#         print(" ", end="")
#     for j in range(0, i*2+1):
#         print("*", end="")
#     print()
# num = 4
# for i in range (0,num):
#     for j in range(1,i+1):
#         print(" ",end='')
#     for k in range(0,2*num-2*i-1):
#         print("*",end='')
#     print()
# num = 4
# for i in range(0,num):
#     for j in range(0,num-i-1):
#         print(" ",end='')
#     for k in range(0,2*i+1):
#         if k%2==0:
#             print("*",end='')
#         else:
#             print(" ",end='')
#     print()
num = 8
for i in range(0,num):
    for j in range(0,num-i-1):
        print(" ",end='')
    for k in range(0,2*i+1):
        if k==0:
            print("*",end='')
        elif k==2*i:
            print("*",end='')
        elif i == num-1:
            print("*",end='')
        else:
            print(" ",end='')
    print()