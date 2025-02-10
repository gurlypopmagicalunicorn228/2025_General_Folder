import calendar
from tkinter import *
import all_constants as c


class Converter():
    """"""
    "Temperature Converter tool ( °C to °F, °F to °C)"
    """"""

    # This part of the code is responsible for the title of the program (Temperature Converter)
    def __init__(self):
        """Temperature Convertor GUI"""
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()
        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font=("Times New Roman", "16", "bold"))

        self.temp_heading.grid(row=0)

        # This part codes for instructions of the GUI Calculator

        instructions = ("Please enter a temperature below, then press one of the buttons to convert to °C/°F. Please "
                        "press help button for more information.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)
        self.temp_entry = Entry(self.temp_frame,
                                font=("Times New Roman", "14",))
        self.temp_entry.grid(row=2, padx=10, pady=10)
        error = "Please enter a number"
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#9C0000")
        self.answer_error.grid(row=3)

        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # Button list  (text|colour|command||row|column)
        button_detail_list = [
            ["To Celcius", "#7C444F", lambda: self.check_temp(c.ABS_ZERO_FARENHEIGHT), 0, 0],
            ["To Farenheight", "#9F5255", lambda: self.check_temp(c.ABS_ZERO_CELCIUS), 0, 1],
            ["Help/Info", "#F39E60", '', 1, 0],
            ["History/Export", "#E16A54", '', 1, 1]
        ]
        # this is a list for the buttons once they have been made
        self.button_ref_list = []
        for item in button_detail_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#FFFFFF", font=("Times New Roman", "12", "bold"),
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(self.make_button)

        # history/export button would be disabled at the start of calculations
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)

    def check_temp(self, min_temp):
        # this codes for valid in the range temp, shows whether It's workable or not/ inputs error
        print("min temp: ", min_temp)

        # retrieve temp to be converted
        to_convert = self.temp_entry.get()
        print("to convert", to_convert)

        # reset label and entry box
        self.answer_error.config(fg="#004C99")
        self.temp_entry.config(bg="#FFFFFF")
        # checks if the chosen temp can be converted in the given range
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp)

        except ValueError:
            error = "enter a number"

        if error != " ":
            self.answer_error.config(text=error, fg="#E44C4C", font=("Times New Roman", "12", "bold"))
            self.temp_entry.config(bg="#F2A0BB")
            self.answer_error.grid(row=3)

    def convert(self, min_temp):
        if min_temp == c.ABS_ZERO_CELCIUS:
            self.answer_error.config(text="Converting to F")
        else:
            self.answer_error.config(text="Converting to C")


# main_routine goes here
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
