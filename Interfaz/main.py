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

# Fecha desde
label_fecha_desde = tk.Label(root, text="Ingrese una fecha desde:", bg="#2b6777", fg="#ffffff", padx=10, pady=10)
label_fecha_desde.grid(row=0, column=0)

calendar_desde = tkc.DateEntry(root, width=10, date_pattern="DD/MM/YYYY", borderwidth=5, state="normal", 
                               background="#f2f2f2", foreground="#2b6777", bordercolor="#2b6777",
                               headersbackground="#c8d8e4",
                               #weekendbackground="#2b6777", weekendforeground="#ffffff",
                               padx=10)
calendar_desde.grid(row=0, column=1)

hora_string = tk.StringVar()
minuto_string = tk.StringVar()
segundo_string = tk.StringVar()

sb_hora = tk.Spinbox(root, from_=0, to=23, width=2, textvariable=hora_string)
sb_hora.grid(row=0, column=2)

sb_minuto = tk.Spinbox(root, from_=0, to=59, width=2, textvariable=minuto_string)
sb_minuto.grid(row=0, column=3)

sb_segundo = tk.Spinbox(root, from_=0, to=59, width=2, textvariable=minuto_string)
sb_segundo.grid(row=0, column=4)



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