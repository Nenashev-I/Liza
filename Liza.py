import tkinter as tk

global counter
counter = 0
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Кто вы?")
        label.pack(side="top", fill="both", expand=True)

        def nClick():
            global counter
            counter += 2
            print(counter)
            btn0.config(state='disabled')
            label.destroy()
            p2 = Page2(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b2 = tk.Button(buttonframe, text="2 вопрос", command=p2.lift)
            b2.pack()

        btn0 = tk.Button(label, text="студент-ботаник", command=nClick)
        btn0.pack()
        btn0.place(relx=0.2, rely=0.6,)

        def OnClick():
            print(counter)
            btn1.config(state='disabled')
            label.destroy()
            p2 = Page2(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b2 = tk.Button(buttonframe, text="2 вопрос", command=p2.lift)
            b2.pack()

        btn1 = tk.Button(label, text="двоечник", command=OnClick)
        btn1.pack()
        btn1.place(relx=0.4, rely=0.6, )


        def OnClick1():
            print(counter)
            btn2.config(state='disabled')
            label.destroy()
            p2 = Page2(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b2 = tk.Button(buttonframe, text="2 вопрос", command=p2.lift)
            b2.pack()
        btn2 = tk.Button(label, text="везунчик",command=OnClick1)
        btn2.pack()
        btn2.place(relx=0.6, rely=0.6, )


        def OnClick2():
            print(counter)
            btn3.config(state='disabled')
            label.destroy()
            p2 = Page2(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b2 = tk.Button(buttonframe, text="2 вопрос", command=p2.lift)
            b2.pack()
        btn3 = tk.Button(label, text="халявщик",command=OnClick2)
        btn3.pack()
        btn3.place(relx=0.8, rely=0.6, )






class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Где вы живите?")
        label.pack(side="top", fill="both", expand=True)
        def nClick3():
            global counter
            counter += 2
            print(counter)
            btn4.config(state='disabled')
            label.destroy()
            p3 = Page3(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b3 = tk.Button(buttonframe, text="3 вопрос", command=p3.lift)
            b3.pack()


        btn4 = tk.Button(label, text="На квартире", command=nClick3)
        btn4.pack()
        btn4.place(relx=0.2, rely=0.6,)

        def OnClick4():
            global counter
            counter += 1
            print(counter)
            btn5.config(state='disabled')
            label.destroy()
            p3 = Page3(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b3 = tk.Button(buttonframe, text="3 вопрос", command=p3.lift)
            b3.pack()
        btn5 = tk.Button(label, text="У родителей", command=OnClick4)
        btn5.pack()
        btn5.place(relx=0.4, rely=0.6, )

        def OnClick5():
            global counter
            counter += 1
            print(counter)
            btn6.config(state='disabled')
            label.destroy()
            p3 = Page3(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b3 = tk.Button(buttonframe, text="3 вопрос", command=p3.lift)
            b3.pack()
        btn6 = tk.Button(label, text="В общежитие",command=OnClick5)
        btn6.pack()
        btn6.place(relx=0.6, rely=0.6, )

class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Как вы провели выходные?")
        label.pack(side="top", fill="both", expand=True)
        def nClick6():
            global counter
            counter += 2
            print(counter)
            btn8.config(state='disabled')
            label.destroy()
            p4 = Page4(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b4 = tk.Button(buttonframe, text="4 вопрос", command=p4.lift)
            b4.pack()

        btn8 = tk.Button(label, text="Усиленно готовился", command=nClick6, anchor='center')
        btn8.pack()
        btn8.place(relx=0.2, rely=0.6,)

        def OnClick7():
            print(counter)
            btn9.config(state='disabled')
            label.destroy()
            p4 = Page4(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b4 = tk.Button(buttonframe, text="4 вопрос", command=p4.lift)
            b4.pack()
        btn9 = tk.Button(label, text="Отдыхал и не парился", command=OnClick7, anchor='center')
        btn9.pack()
        btn9.place(relx=0.4, rely=0.6, )

        def OnClick8():
            global counter
            counter += 1
            print(counter)
            btn10.config(state='disabled')
            label.destroy()
            p4 = Page4(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b4 = tk.Button(buttonframe, text="4 вопрос", command=p4.lift)
            b4.pack()
        btn10 = tk.Button(label, text="Прочитал пару билетов",command=OnClick8, anchor='center')
        btn10.pack()
        btn10.place(relx=0.6, rely=0.6, )

        def OnClick9():
            print(counter)
            btn11.config(state='disabled')
            label.destroy()
            p4 = Page4(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b4 = tk.Button(buttonframe, text="4 вопрос", command=p4.lift)
            b4.pack()
        btn11 = tk.Button(label, text="Тусовался все выходные",command=OnClick9, anchor='center')
        btn11.pack()
        btn11.place(relx=0.8, rely=0.6, )

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Попросите ли вы помощи у одногрупников?")
        label.pack(side="top", fill="both", expand=True)
        def nClick10():
            global counter
            counter += 2
            print(counter)
            btn12.config(state='disabled')
            label.destroy()
            p5 = Page5(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b5 = tk.Button(buttonframe, text="5 вопрос", command=p5.lift)
            b5.pack()

        btn12 = tk.Button(label, text="Да", command=nClick10)
        btn12.pack()
        btn12.place(relx=0.2, rely=0.6,)

        def OnClick11():
            print(counter)
            btn13.config(state='disabled')
            label.destroy()
            p5 = Page5(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b5 = tk.Button(buttonframe, text="5 вопрос", command=p5.lift)
            b5.pack()
        btn13 = tk.Button(label, text="нет", command=OnClick11)
        btn13.pack()
        btn13.place(relx=0.4, rely=0.6, )

class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Во сколько вы ляжете спать?")
        label.pack(side="top", fill="both", expand=True)

        def nClick12():
            global counter
            counter += 2
            print(counter)
            btn14.config(state='disabled')
            label.destroy()
            p6 = Page6(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b6 = tk.Button(buttonframe, text="6 вопрос", command=p6.lift)
            b6.pack()

        btn14 = tk.Button(label, text="В 23:00", command=nClick12)
        btn14.pack()
        btn14.place(relx=0.2, rely=0.6,)

        def OnClick13():
            global counter
            counter += 1
            print(counter)
            btn15.config(state='disabled')
            label.destroy()
            p6 = Page6(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b6 = tk.Button(buttonframe, text="6 вопрос", command=p6.lift)
            b6.pack()
        btn15 = tk.Button(label, text="В 1 ночи", command=OnClick13)
        btn15.pack()
        btn15.place(relx=0.4, rely=0.6, )

        def OnClick14():
            print(counter)
            btn16.config(state='disabled')
            label.destroy()
            p6 = Page6(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b6 = tk.Button(buttonframe, text="6 вопрос", command=p6.lift)
            b6.pack()
        btn16 = tk.Button(label, text="В 3 утра",command=OnClick14)
        btn16.pack()
        btn16.place(relx=0.6, rely=0.6, )

        def OnClick15():
            print(counter)
            btn17.config(state='disabled')
            label.destroy()
            p6 = Page6(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b6 = tk.Button(buttonframe, text="6 вопрос", command=p6.lift)
            b6.pack()
        btn17 = tk.Button(label, text="Сон не для меня",command=OnClick15)
        btn17.pack()
        btn17.place(relx=0.8, rely=0.6, )

class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Ваш будильник звонит, что вы сделаете?")
        label.pack(side="top", fill="both", expand=True)

        def nClick16():
            global counter
            counter += 2
            print(counter)
            btn18.config(state='disabled')
            label.destroy()
            p7 = Page7(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b7 = tk.Button(buttonframe, text="7 вопрос", command=p7.lift)
            b7.pack()

        btn18 = tk.Button(label, text="Выключу и буду собираться", command=nClick16)
        btn18.pack()
        btn18.place(relx=0.2, rely=0.6,)

        def OnClick17():
            global counter
            counter += 1
            print(counter)
            btn19.config(state='disabled')
            label.destroy()
            p7 = Page7(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b7 = tk.Button(buttonframe, text="7 вопрос", command=p7.lift)
            b7.pack()
        btn19 = tk.Button(label, text="Отложу на 10 минут", command=OnClick17)
        btn19.pack()
        btn19.place(relx=0.4, rely=0.6, )

        def OnClick18():
            print(counter)
            btn20.config(state='disabled')
            p7 = Page7(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            label.destroy()
            p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b7 = tk.Button(buttonframe, text="7 вопрос", command=p7.lift)
            b7.pack()
        btn20 = tk.Button(label, text='Выключу и полежу ещё "минутку"',command=OnClick18)
        btn20.pack()
        btn20.place(relx=0.6, rely=0.6, )


class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Стоит ли подучить материал по пути в университет?")
        label.pack(side="top", fill="both", expand=True)

        def nClick19():
            global counter
            counter += 2
            print(counter)
            btn21.config(state='disabled')
            label.destroy()
            p8 = Page8(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b8 = tk.Button(buttonframe, text="8 вопрос", command=p8.lift)
            b8.pack()

        btn21 = tk.Button(label, text="Да, конечно", command=nClick19)
        btn21.pack()
        btn21.place(relx=0.2, rely=0.6,)

        def OnClick20():
            global counter
            counter += 1
            print(counter)
            btn22.config(state='disabled')
            label.destroy()
            p8 = Page8(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b8 = tk.Button(buttonframe, text="2 вопрос", command=p8.lift)
            b8.pack()
        btn22 = tk.Button(label, text="Повторю основные формулы", command=OnClick20)
        btn22.pack()
        btn22.place(relx=0.4, rely=0.6, )

        def OnClick21():
            print(counter)
            btn23.config(state='disabled')
            label.destroy()
            p8 = Page8(self)
            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)
            p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            b8 = tk.Button(buttonframe, text="8 вопрос", command=p8.lift)
            b8.pack()
        btn23 = tk.Button(label, text="Нет",command=OnClick21)
        btn23.pack()
        btn23.place(relx=0.6, rely=0.6, )

class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Попытаться списать?")
        label.pack(side="top", fill="both", expand=True)
        def nClick22():
            print(counter)
            btn25.config(state='disabled')

        btn25 = tk.Button(label, text="Да", command=nClick22)
        btn25.pack()
        btn25.place(relx=0.2, rely=0.6,)

        def OnClick23():
            global counter
            counter += 2
            print(counter)
            btn26.config(state='disabled')
        btn26 = tk.Button(label, text="Нет", command=OnClick23)
        btn26.pack()
        btn26.place(relx=0.4, rely=0.6, )

        def OnClick24():
            Canvas = tk.Canvas()
            Canvas.pack()

            frame = tk.Frame()
            frame.place(relx=0, rely=0, relheight=1, relwidth=1)
            if counter == 0:
                label = tk.Label(frame, text="Вы не сдали экзамен!!!")
                label.pack(side="top", fill="both", expand=True)
            elif counter <= 4:
                label = tk.Label(frame, text="Вы сдали экзамен на: 25 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 5:
                label = tk.Label(frame, text="Вы сдали экзамен на: 40 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 6:
                label = tk.Label(frame, text="Вы сдали экзамен на: 50 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 7:
                label = tk.Label(frame, text="Вы сдали экзамен на: 60 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 8:
                label = tk.Label(frame, text="Вы сдали экзамен на: 65 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 9:
                label = tk.Label(frame, text="Вы сдали экзамен на: 65 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 8:
                label = tk.Label(frame, text="Вы сдали экзамен на: 70 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 10:
                label = tk.Label(frame, text="Вы сдали экзамен на: 75 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 11:
                label = tk.Label(frame, text="Вы сдали экзамен на: 80 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 12:
                label = tk.Label(frame, text="Вы сдали экзамен на: 85 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 13:
                label = tk.Label(frame, text="Вы сдали экзамен на: 90 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter == 14:
                label = tk.Label(frame, text="Вы сдали экзамен на: 95 баллов ")
                label.pack(side="top", fill="both", expand=True)
            elif counter >= 15:
                label = tk.Label(frame, text="Вы сдали экзамен на: 100 баллов ")
                label.pack(side="top", fill="both", expand=True)

            print(counter)
            btn27.config(state='disabled')
        btn27 = tk.Button(label, text="Итог", command=OnClick24)
        btn27.pack()
        btn27.place(relx=0.8, rely=0.8, )

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)
        p8 = Page8(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="1 вопрос", command=p1.lift)
        b2 = tk.Button(buttonframe, text="2 вопрос", command=p2.lift)
        b3 = tk.Button(buttonframe, text="3 вопрос", command=p3.lift)
        b4 = tk.Button(buttonframe, text="4 вопрос", command=p4.lift)
        b5 = tk.Button(buttonframe, text="5 вопрос", command=p5.lift)
        b6 = tk.Button(buttonframe, text="6 вопрос", command=p6.lift)
        b7 = tk.Button(buttonframe, text="7 вопрос", command=p7.lift)
        b8 = tk.Button(buttonframe, text="8 вопрос", command=p8.lift)


        p1.show()



if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1000x1000")


    root.mainloop()

