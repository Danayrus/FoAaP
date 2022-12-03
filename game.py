from tkinter import *
slovar = {1 : "У многих великих и не очень путешественников приключения начинаются с маленькой деревушки, награду получаешь маленькую, зато монстры здесь не так опасны.",
          2 : "Вы не стали исключением в этой давней «традиции».\n Ваше приключение началось с маленькой деревушки под названием Варвуд. В данный момент вы сидите в таверне и слушаете сплетни бармена. Мало ли вам найдется какая работенка."}
index = 0
def mainwindow():
    backg.grid(row=0, column=0)
    textbox.place(rely=0.7, relwidth=1, relheight=0.25) # Расположение текстбокса
    textq.place(relx=0.15,relwidth=0.85) # расположение текста
    person_image.place(relwidth=0.15)
    button_choise1.place(x=120, y= 300)
    button_choise2.place(x=340, y=300)
def bchoise1():
    index = story[index][1]
def bchoise2():

def starttext():
    textq.insert('1.0', "У многих великих и не очень путешественников приключения начинаются с маленькой деревушки, награду получаешь маленькую, зато монстры здесь не так опасны.")
    textq.insert(END, '\nВы не стали исключением в этой давней «традиции».\n Ваше приключение началось с маленькой деревушки под названием Варвуд. В данный момент вы сидите в таверне и слушаете сплетни бармена. Мало ли вам найдется какая работенка.')

window = Tk() #Окно приложения
window.geometry("960x540")
window.title('Текстовый квест')
window.resizable(width=False, height= False)
window.iconbitmap('Background.ico')
mainbg = PhotoImage(file= 'Background.png')
person = PhotoImage(file='person.png')
backg = Label(window,image=mainbg)
textbox = Frame(window, bg = 'pink') # Текстбокс
textq =Text(textbox,bg='pink', font=("Times New Roman",14)) # Текст в текстбоксе
person_image = Label(textbox, image=person)
button_choise1 = Button(window, text='Выбор1') # Кнопка выбора
button_choise2 = Button(window, text='Выбор2')

mainwindow() # Вызов главного окна
starttext()
## Сюжет
story = [
    ['Text1',1,1],
    ['Text2',0,2],
    ['Text3',1,3],
    ['Text4',2,0]
]


window.mainloop()