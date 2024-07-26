import tkinter as tk
from tkinter import messagebox

def click(event):
  text = event.widget.cget("text")
  if text == "=":
      try:
          result = str(eval(screen.get()))
          screen.set(result)
      except Exception as e:
          messagebox.showerror("Hata", "Geçersiz İşlem")
          screen.set("")
  elif text == "C":
      screen.set("")
  else:
      screen.set(screen.get() + text)

root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("600x800")
root.resizable(0, 0)
root.configure(bg="#1e1e1e")

# Gradient background for the main window
canvas = tk.Canvas(root, width=600, height=800)
canvas.pack(fill="both", expand=True)

# Create gradient background
gradient = canvas.create_rectangle(0, 0, 600, 800, fill="", outline="")
canvas.itemconfig(gradient, fill="")

# Function to create gradient
def create_gradient(canvas, item, color1, color2):
  steps = 100
  r1, g1, b1 = canvas.winfo_rgb(color1)
  r2, g2, b2 = canvas.winfo_rgb(color2)
  r_ratio = (r2 - r1) / steps
  g_ratio = (g2 - g1) / steps
  b_ratio = (b2 - b1) / steps

  for i in range(steps):
      nr = int(r1 + (r_ratio * i))
      ng = int(g1 + (g_ratio * i))
      nb = int(b1 + (b_ratio * i))
      color = f'#{nr:04x}{ng:04x}{nb:04x}'
      canvas.create_rectangle(0, i * 8, 600, (i + 1) * 8, fill=color, outline=color)

create_gradient(canvas, gradient, "#ff7e5f", "#feb47b")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 30 bold", bg="#2e2e2e", fg="#ffffff", bd=0, justify="right", highlightthickness=0)
entry_window = canvas.create_window(300, 100, window=entry, width=580, height=80)

buttons = [
  '7', '8', '9', '/',
  '4', '5', '6', '*',
  '1', '2', '3', '-',
  'C', '0', '=', '+'
]

frame = tk.Frame(root, bg="#1e1e1e")
frame_window = canvas.create_window(300, 500, window=frame, width=580, height=600)

for i, button in enumerate(buttons):
  btn = tk.Button(frame, text=button, font="lucida 20 bold", bg="#3e3e3e", fg="#ffffff", bd=0, padx=30, pady=30, highlightthickness=0, relief="flat")
  btn.grid(row=i//4, column=i%4, padx=10, pady=10, sticky="nsew")
  btn.bind("<Button-1>", click)

# Grid layout configuration for equal button sizes
for i in range(4):
  frame.grid_columnconfigure(i, weight=1)
  frame.grid_rowconfigure(i, weight=1)

root.mainloop()