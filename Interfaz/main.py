import tkinter as tk
import tkcalendar as tkc
from datetime import datetime

root = tk.Tk()
root.title("Pantalla de prueba")
root.config(bg="#2b6777")
root.geometry("1500x600+200+200")

today = datetime.today()

def confirm_date():
    fecha = calendar_desde.get_date()
    print(fecha.day)

def validar_numeros(*args):
    hora = hora_string.get()
    minuto = minuto_string.get()
    segundo = segundo_string.get()
    
    print(f"{hora}:{minuto}:{segundo}")
    
    if not hora.isnumeric() and hora != "":
        hora_string.set(0)
    if not minuto.isnumeric() and minuto != "":
        minuto_string.set(0)
    if not segundo.isnumeric() and segundo != "":
        segundo_string.set(0)
        

# Fecha desde
label_fecha_desde = tk.Label(root, text="Ingrese una fecha desde:", bg="#2b6777", fg="#ffffff", padx=10, pady=10)
label_fecha_desde.grid(row=0, column=0)

calendar_desde = tkc.DateEntry(root, width=10, date_pattern="DD/MM/YYYY", borderwidth=5, state="normal", 
                               background="#f2f2f2", foreground="#2b6777", bordercolor="#2b6777",
                               headersbackground="#c8d8e4",
                               #weekendbackground="#2b6777", weekendforeground="#ffffff",
                               padx=10)
calendar_desde.grid(row=0, column=1)

hora_string = tk.StringVar(root)
minuto_string = tk.StringVar(root)
segundo_string = tk.StringVar(root)

hora_hasta_string = tk.StringVar(root)
minuto_hasta_string = tk.StringVar(root)
segundo_hasta_string = tk.StringVar(root)

sb_hora = tk.Spinbox(root, from_=0, to=23, width=3, textvariable=hora_string, wrap=True)
sb_hora.grid(row=0, column=2)

hora_string.trace("w", validar_numeros)

sb_minuto = tk.Spinbox(root, from_=0, to=59, width=3, textvariable=minuto_string)
sb_minuto.grid(row=0, column=3)

minuto_string.trace("w", validar_numeros)

sb_segundo = tk.Spinbox(root, from_=0, to=59, width=3, textvariable=segundo_string)
sb_segundo.grid(row=0, column=4)

segundo_string.trace("w", validar_numeros)



button_fecha_desde = tk.Button(root, text="Confirmar", command=confirm_date)
button_fecha_desde.grid(row=1, column=0)

# Fecha hasta
# label_fecha_desde = tk.Label(root, text="Ingrese una fecha hasta:", bg="#2b6777", fg="#ffffff", padx=10, pady=10)
# label_fecha_desde.grid(row=1, column=0)

# fecha_hasta_entry = tk.Entry(root, width=14)
# fecha_hasta_entry.grid(row=0, column=3)

# calendar_hasta = tkc.Calendar(root, selectmode="day", year=today.year, month=today.month, day=today.day, borderwidth=5, state="normal", background="#375362", bordercolor="#375362")
# calendar_hasta.grid(row=1, column=2, columnspan=2, padx=10)






root.mainloop()