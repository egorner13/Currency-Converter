import tkinter as tk
import tkinter.font as font
import currencies


class MyGui:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, height=400, width=400, background="dark green")
        self.canvas.pack()

        self.outer_frame = tk.Frame(self.master, background="light green")
        self.outer_frame.place(relheight=.8, relwidth=.8, relx=.1, rely=.1)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.place(relheight=.1, relwidth=.8, relx=.1, rely=.4)

        self.intro_button = tk.Button(self.button_frame, text="Click here to start", height=40, width=30,
                                      background="white", foreground="dark green", command=self.page_two)
        self.intro_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.intro_button['font'] = self.intro_button_font
        self.intro_button.pack()

    def page_two(self):
        self.button_frame.configure(background="dark green")
        self.intro_button.destroy()

        self.yes_button_frame = tk.Frame(self.master, background="light green")
        self.yes_button_frame.place(relheight=.1, relwidth=.4, relx=.3, rely=.6)

        self.no_button_frame = tk.Frame(self.master, background="light green")
        self.no_button_frame.place(relheight=.1, relwidth=.4, relx=.3, rely=.8)

        self.text = tk.Label(self.button_frame, text="Start a currency conversion?", height=40, width=30,
                             background="white", foreground="dark green")
        self.text_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.text['font'] = self.text_font

        self.text.pack()

        self.yes_button = tk.Button(self.yes_button_frame, text="Yes", height=40, width=30,
                                    background="gray", foreground="dark green", command=self.page_yes)
        self.yes_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.yes_button['font'] = self.yes_button_font
        self.yes_button.pack()

        self.no_button = tk.Button(self.no_button_frame, text="No", height=40, width=30,
                                   background="gray", foreground="dark green", command=self.page_no)
        self.no_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.no_button['font'] = self.no_button_font
        self.no_button.pack()

    def page_yes(self):
        self.yes_button.destroy()
        self.no_button.destroy()

        self.text.destroy()
        self.text = tk.Label(self.button_frame, text="Select currency to convert from", height=40, width=40,
                             background="white", foreground="dark green")
        self.text_font = font.Font(family="Helvetica", size=13, weight="bold")
        self.text['font'] = self.text_font

        self.text.pack()

        self.clicked = tk.StringVar()
        self.clicked.set("US Dollar")

        self.options = tk.OptionMenu(self.yes_button_frame, self.clicked, *currencies.curr_list())
        self.options.config(width=40, height=40)
        self.options.pack()

        self.no_button = tk.Button(self.no_button_frame, text="Continue", height=40, width=30,
                                   background="gray", foreground="dark green", command=self.sec_page_next)
        self.no_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.no_button['font'] = self.no_button_font
        self.no_button.pack()

    def sec_page_next(self):
        self.first = self.clicked.get()
        self.first_value = currencies.value(self.first)

        self.no_button.destroy()
        self.text.destroy()
        self.text = tk.Label(self.button_frame, text="Select currency to convert to", height=40, width=40,
                             background="white", foreground="dark green")
        self.text_font = font.Font(family="Helvetica", size=13, weight="bold")
        self.text['font'] = self.text_font

        self.text.pack()

        self.no_button = tk.Button(self.no_button_frame, text="Continue", height=40, width=30,
                                   background="gray", foreground="dark green", command=self.final_page)
        self.no_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.no_button['font'] = self.no_button_font
        self.no_button.pack()

    def final_page(self):
        self.second = self.clicked.get()
        self.second_value = currencies.value(self.second)

        self.conversion = self.second_value / self.first_value

        self.no_button.destroy()
        self.text.destroy()

        self.final_frame = tk.Frame(self.master)
        self.final_frame.place(relheight=.2, relwidth=.8, relx=.1, rely=.1)

        self.text = tk.Label(self.final_frame, text="The conversion rate for 1\n " + self.first +
                                                    " is\n " + str(round(self.conversion, 2)) + " "
                                                    + self.second,
                             height=40, width=40, background="white", foreground="dark green")
        self.text_font = font.Font(family="Helvetica", size=13, weight="bold")
        self.text['font'] = self.text_font

        self.text.pack()

        self.more_text = tk.Label(self.button_frame, text="Do another currency conversion?", height=40, width=40,
                                  background="white", foreground="dark green")
        self.more_text_font = font.Font(family="Helvetica", size=13, weight="bold")
        self.more_text['font'] = self.more_text_font

        self.more_text.pack()

        self.options.destroy()

        self.yes_button = tk.Button(self.yes_button_frame, text="Yes", height=40, width=30,
                                    background="gray", foreground="dark green", command=self.another)
        self.yes_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.yes_button['font'] = self.yes_button_font
        self.yes_button.pack()

        self.no_button = tk.Button(self.no_button_frame, text="No", height=40, width=30,
                                   background="gray", foreground="dark green", command=self.page_no)
        self.no_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.no_button['font'] = self.no_button_font
        self.no_button.pack()

    def another(self):
        self.final_frame.destroy()
        self.no_button.destroy()
        self.more_text.destroy()
        self.yes_button.destroy()

        self.text = tk.Label(self.button_frame, text="Click below to continue", height=40, width=40,
                             background="white", foreground="dark green")
        self.text_font = font.Font(family="Helvetica", size=13, weight="bold")
        self.text['font'] = self.more_text_font

        self.text.pack()

        self.yes_button = tk.Button(self.yes_button_frame, text="Continue", height=40, width=30,
                                    background="gray", foreground="dark green", command=self.page_yes)
        self.yes_button_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.yes_button['font'] = self.yes_button_font
        self.yes_button.pack()

    def page_no(self):
        self.master.destroy()
