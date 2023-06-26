import tkinter as tk
from tkinter import messagebox
from math import log10, pow

class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced dB, dBm and Watts Converter")
        self.geometry("600x300")

        # Menubar
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="ReadMe", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

        # UI Elements
        self.label = tk.Label(self, text="Enter value:")
        self.label.grid(row=0, column=0, padx=(20, 0), pady=20)

        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1, padx=(0, 20), pady=20)

        self.var_from = tk.StringVar(self)
        self.var_from.set("dBm")

        self.option_menu_from = tk.OptionMenu(self, self.var_from, "dBm", "dB", "Watts")
        self.option_menu_from.grid(row=0, column=2, padx=20, pady=20)

        self.var_to = tk.StringVar(self)
        self.var_to.set("Watts")

        self.option_menu_to = tk.OptionMenu(self, self.var_to, "dBm", "dB", "Watts")
        self.option_menu_to.grid(row=0, column=3, padx=20, pady=20)

        self.result_label = tk.Label(self, text="Result: ", font=("Courier", 10))
        self.result_label.grid(row=2, column=0, columnspan=4, pady=(0, 20))

        self.result_mW_label = tk.Label(self, text="", font=("Courier", 10))
        self.result_mW_label.grid(row=3, column=0, columnspan=4)

        self.result_uW_label = tk.Label(self, text="", font=("Courier", 10))
        self.result_uW_label.grid(row=4, column=0, columnspan=4)

        self.result_nW_label = tk.Label(self, text="", font=("Courier", 10))
        self.result_nW_label.grid(row=5, column=0, columnspan=4)

        self.formula_label = tk.Label(self, text="Formula: ", font=("Courier", 10))
        self.formula_label.grid(row=6, column=0, columnspan=4)

        self.calc_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calc_button.grid(row=1, column=1, columnspan=2, pady=20)

        self.clear_button = tk.Button(self, text="Clear", command=self.clear)
        self.clear_button.grid(row=1, column=3, pady=20)

    def calculate(self):
        input_value = self.entry.get()
        from_unit = self.var_from.get()
        to_unit = self.var_to.get()

        if not input_value:
            messagebox.showerror("Input Error", "Please input a value!")
            return

        try:
            input_value = float(input_value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a numerical value!")
            return

        if from_unit == "dBm" and to_unit == "Watts":
            result = pow(10, (input_value - 30) / 10)
            formula = "10^((dBm - 30) / 10)"
            result_mW = result * 1000
            result_uW = result * 1e6
            result_nW = result * 1e9
        elif from_unit == "Watts" and to_unit == "dBm":
            result = 10 * log10(input_value * 1000)
            formula = "10 * log10(Watts * 1000)"
        elif from_unit == "dB" and to_unit == "dBm":
            result = input_value + 30
            formula = "dB + 30"
        elif from_unit == "dBm" and to_unit == "dB":
            result = input_value - 30
            formula = "dBm - 30"
        else:
            messagebox.showerror("Input Error", "Invalid conversion!")
            return

        self.result_label.config(text=f"Result: {result:.10f} {to_unit}")
        if to_unit == "Watts":
            self.result_mW_label.config(text=f"Result: {result_mW:.10f} mW")
            self.result_uW_label.config(text=f"Result: {result_uW:.10f} µW")
            self.result_nW_label.config(text=f"Result: {result_nW:.10f} nW")
        else:
            self.result_mW_label.config(text="")
            self.result_uW_label.config(text="")
            self.result_nW_label.config(text="")
        self.formula_label.config(text=f"Formula: {formula}")

    def clear(self):
        self.entry.delete(0, 'end')
        self.result_label.config(text="Result: ")
        self.result_mW_label.config(text="")
        self.result_uW_label.config(text="")
        self.result_nW_label.config(text="")
        self.formula_label.config(text="Formula: ")

    def show_about(self):
        about_window = tk.Toplevel(self)
        about_window.title("About")
        about_label = tk.Label(about_window, text=
    """Advanced dB, dBm and Watts Converter

    This application provides a simple and intuitive interface for converting between different units of power measurement, namely decibels (dB), dBm (decibel-milliwatts), and Watts.

    Features:
    - User-friendly design: The interface of the application is designed to be user-friendly, making it easy for users to understand and use.
    - Multiple units: The application supports conversion between dB, dBm, and Watts.
    - Instant results: As soon as you click 'Calculate', the application instantly provides the result of the conversion.

    How to use:
    - Input your value in the entry box next to 'Enter value:'. This value represents the magnitude of the power you want to convert.
    - Select the unit of the value you just input from the drop-down menu next to the entry box.
    - Select the unit you want to convert to from the second drop-down menu.
    - Click 'Calculate' to get the result. The result of the conversion will be displayed, as well as the formula used for the conversion.
    - Click 'Clear' to reset the input field and result.

    This application is perfect for students, engineers, scientists, or anyone needing to frequently convert between dB, dBm, and Watts. Remember to input the values appropriately, as the application does not check whether the conversion between the selected units is meaningful.

    Enjoy converting!"""
    )
        about_label.pack(padx=20, pady=20)


if __name__ == "__main__":
    app = Converter()
    app.mainloop()
