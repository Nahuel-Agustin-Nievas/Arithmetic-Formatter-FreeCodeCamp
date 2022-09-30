def arithmetic_arranger(problems, sol = False):
    primero = ""
    segundo = ""
    lineas = ""
    sumar= ""
    arranged_problems = ""
    
# problemas no pueden ser mas de 5
    if len(problems) > 5:
            arranged_problems = "Error: Too many problems."
            return arranged_problems

            

    for problem in problems:
         num1 = problem.split(" ")[0]
         num2 = problem.split(" ")[1]
         num3 = problem.split(" ")[2] 
         #problemas no pueden tener otro operador que no sea + o -
         if not (num2 in ("+", "-")):
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        #cuentas deben ser solo digitos
         if num1.isdigit() == False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
         elif num3.isdigit() == False:
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems

        #numeros no pueden ser mayor a 5
         if len(num1) >=5 :
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

         elif len(num3) >=5 :
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems

         operation = ""
         if num2 == "+":
              operation =  str(int(num1) + int(num3))
         elif num2 == "-":
              operation =  str(int(num1) - int(num3))
             

         length = max(len(num1), len(num3)) + 2
         arriba = str(num1).rjust(length)
         abajo = num2 + str(num3).rjust(length - 1)
         linea = "-" * (length)
         resultado = str(operation).rjust(length)

        
         primero += arriba + "    "
         segundo += abajo + "    "
         lineas += linea + "    "
         sumar += resultado + "    "
         

             
    if sol:
        arranged_problems = primero + "\n" + segundo + "\n" + lineas + "\n" + sumar
    else:
       arranged_problems = primero + "\n" + segundo + "\n" + lineas


       return arranged_problems


#test
#arithmetic_arranger(["32 + 698", "1 - 3801", "9999 + 9999", "43 - 49", "523 - 49"])
