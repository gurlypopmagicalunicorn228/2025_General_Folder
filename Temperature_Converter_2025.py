#demo?
from calendar import error
from tkinter import *
class Converter():
    """"""
    "Temperature Converter tool ( °C to °F, °F to °C)"
    """"""

    def __init__(self):
        """Temperature Convertor GUI"""
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font= ("Times New Roman", "16", "bold"))



        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press one of the buttons to convert")
        self.temp_instructions = Label(self.temp_frame,
                                       text = "Instructions",
                                       wraplength=250, width= 40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        self.temp_entry = Entry(self.temp_frame,
                                font=("Times New Roman", "14",))
        self.temp_entry.grid(row=2,padx=10,pady=10)
        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame,text = error,
                                fg = "#9C0000")
        self.temp_error.grid(row=3)
        # Conversion, help & History/ Export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celcius_button = Button(self.button_frame,
                                    text="To Celcius",
                                    bg="#7C444F",
                                    fg="#ffffff",
                                    font=("Times New Roman", "12", "bold"), width=12)
        self.to_celcius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_farenheight_button = Button(self.button_frame,
                                            text="To Farengheight",
                                            bg="#9F5255",
                                            fg="#ffffff",
                                            font=("Times New Roman", "12", "bold"), width=12)
        self.to_farenheight_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame,
                                            text="To Help",
                                            bg="#E16A54",
                                            fg="#ffffff",
                                            font=("Times New Roman", "12", "bold"), width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame,
                                            text="To History",
                                            bg="#F39E60",
                                            fg="#ffffff",
                                            font=("Times New Roman", "12", "bold"), width=12)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


#main_routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter ()
    root.mainloop()
