import tkinter as tk
from calculate import add,subtract,multiply,divide

def operation(op):
    try:
        num1 = int(entry1.get())
        num2 =int(entry2.get())
        if op == "add":
            result = add(num1, num2)
        elif op == "subtract":
            result = subtract(num1, num2)
        elif op == "multiply":
            result = multiply(num1, num2)
        elif op == "divide":
            result = divide(num1, num2)

        labelResult.config(text=f"Result: {result}", fg='green',font=('sans-serif',16,'bold'))

    except ZeroDivisionError:
        labelResult.config(text="Error: Cannot divide by zero", fg='red',font=('sans-serif',16,'bold'))
    except ValueError:
        labelResult.config(text="Error: Invalid numeric input", fg='red',font=('sans-serif',16,'bold'))
    except ValueError:
      raise ValueError("Input must be a number")
    except Exception:
        labelResult.config(text="Unexpected Error", fg='red',font=('sans-serif',16,'bold'))


root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

labelNum1 = tk.Label(root, text="Enter num1:",fg="#ff0000",font=('Arial',14))
labelNum1.grid(row=0,column=0, padx=15,pady=15)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

labelNum2 = tk.Label(root, text="Enter num2:",fg="#ff0101",font=('Arial',14))
labelNum2.grid(row=1, column=0, padx=15,pady=15)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

btn = tk.Button(root, text="Addition", width=10, command=lambda: operation("add"),bg="#4CAF50",fg="white",font=("Arial",12))
btn.grid(row=2, column=0,padx=5,pady=5)
btn = tk.Button(root, text="Subtraction", width=10, command=lambda: operation("subtract"),bg="#4CAF50",fg="white",font=("Arial",12))
btn.grid(row=2, column=1,padx=5,pady=5)
btn = tk.Button(root, text="Multiplication", width=10, command=lambda: operation("multiply"),bg="#4CAF50",fg="white",font=("Arial",12))
btn.grid(row=3, column=0,padx=5,pady=5)
btn = tk.Button(root, text="Division", width=10, command=lambda: operation("divide"),bg="#4CAF50",fg="white",font=("Arial",12))
btn.grid(row=3, column=1,padx=5,pady=5)

labelResult = tk.Label(root, text="Result:")
labelResult.grid(row=4, column=0, columnspan=2,pady=20)

root.mainloop()