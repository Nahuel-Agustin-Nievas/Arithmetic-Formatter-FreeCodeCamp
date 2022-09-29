# from curses.ascii import isdigit


def arithmetic_arranger(problems):

    primero = ""
    segundo = ""
    lineas = ""
    sumar= ""
    string = ""

    if len(problems) > 5:
            arranged_problems = "Error: Too many problems."
            return arranged_problems
            # print("error mas de 5 problemas")

    for problem in problems:
         num1 = problem.split(" ")[0]
         num2 = problem.split(" ")[1]
         num3 = problem.split(" ")[2]

         if not (num2 in ("+", "-")):
            arranged_problems = "Error: Operator must be '+' or '-'."
            
            # print("error debe ser + o -")

         if num1.isdigit() == False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
         elif num3.isdigit() == False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
           # error de caracter que no se numerico
            
         
         


    



    
    # return arranged_problems



# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 / 9999", "523 - 49", "523 - 49", "523 - 49"])

arithmetic_arranger(["7 + 7", "7 - 3801", "9999 + 9999", "523 + 49"])
 



# num = 60

# strin = "hola"

# print (type(num))
# print (type(strin))



# def check (a):
#     if type(a) == str:
#         print( a + " es un string")
#     else :
#         print (str(a) + " Es un numero")




# check(strin)
# check(num)


# num1 = "+"
# num2= "-"
# num3 = "*"
# num4= 5
# num5 = "7 8 8"

# print(num1)
# print(num2)
# print(num3)
# print (type(num4))
# print (type(num5))


# num6 = num5.split(" ")
# print(num6)

# num7 = num6[0]
# num8= num6[1]
# print(num7)
# print(num8)

# print (type(num7))
# print (num7.isdigit())
# print (num8.isdigit())

# if num7.isdigit() == True:
#     print("Es un num")


# def check (a,b):
#     if a.isdigit()  == False :
#         print ("No es un num en la funcion")
#     elif  b.isdigit() == False:
#         print ("No es un num en la funcion 2")
#     else :
#         print ("es un num fun")


# check (num7, num8)


# if type(num4) != int:
#     print("es distinto a un numero")
# else :
#     print( "es un nume")


# # if (num1 != "+") or (num1 != "-") :
# #     print("es distino")
# # else:
# #     print("es un simbolo")


# # if not (operator[0] in ('-','+') ):
# #         return "Error: Operator must be '+' or '-'."

# if not (num2 in ("+", "-")):
#     print("es distino")
# else:
#     print("es un simbolo")