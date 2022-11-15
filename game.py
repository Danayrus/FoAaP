from tkinter import *
def inventory():
    backg.grid_forget()
    backg_inventory.grid(row=0, column=0)
    button_inventory.place_forget()
    textbox.place_forget()
    button_main.place(x=1, y=513)
def mainwindow():
    backg_inventory.grid_forget()
    backg.grid(row=0, column=0)
    button_inventory.place(relx=0.85, rely=0.7, relwidth=0.15, relheight=0.25) # Расположение кнопки инвентаря
    textbox.place(rely=0.7, relwidth=0.85, relheight=0.25) # Расположение текстбокса
    textq.pack(side=RIGHT) # расположение текста
    button_main.place_forget()


window = Tk() #Окно приложения
window.geometry("960x540")
window.title('Текстовый квест')
window.resizable(width=False, height= False)
window.iconbitmap('Background.ico')
menubg = PhotoImage(file='Menu.png')
mainbg = PhotoImage(file= 'Background.png')
backg = Label(window,image=mainbg)
backg_inventory = Label(window,image=menubg)
textbox = Frame(window, bg = 'pink') # Текстбокс
textq =Text(textbox,bg='pink', font=("Times New Roman",14)) # Текст в текстбоксе
textq.insert('1.0', "Привет")
textq.insert(END, '\nПока')
button_choise = Button() # Кнопка выбора
button_main = Button(window, text='Назад',command=mainwindow) # Выход из инвентаря к текстбоксу
button_inventory =Button(window, text='Инвентарь',command=inventory) # Кнопка инвентаря
mainwindow() # Вызов главного окна



window.mainloop()