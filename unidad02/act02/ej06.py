num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /, **): ")

match operacion:
    case "+":
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")

    case "-":
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")

    case "*" | "x":
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")

    case "/":
        if num2 == 0:
            print("Error: no se puede dividir entre 0")
        else:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")

    case "**":
        resultado = num1 ** num2
        print(f"{num1} ** {num2} = {resultado}")

    case _:
        print("Operación no válida")