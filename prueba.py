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
            return arranged_problems
            # print("error debe ser + o -")
            
         
         


    



    
    # return arranged_problems



arithmetic_arranger(["32 + 8", "1 - 3801", "9999 / 9999", "523 - 49", "523 - 49", "523 - 49"])

# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 + 49"])
 



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

# print(num1)
# print(num2)
# print(num3)

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