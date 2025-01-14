import random
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox
import tkinter


class MainApplication(tkinter.Frame):
    def __init__(self, parent, *args, **kwargs) -> None:
        """
        Create graphical interface

        Parameters:
            self: Main tkinter frame
            parent:
            args:
            kwargs:

        Returns:
            None

        """
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.counter = int(0)
        self.combo_value = str(None)
        self.label = tkinter.Label(self)
        self.label2 = tkinter.Label(self)
        self.entry = tkinter.Entry(self)
        self.button = tkinter.Button(self, text="Submit", command=self.levels)
        self.label3 = tkinter.Label(self)

        self.difficulty_combo = (
            tkinter.ttk.Combobox(self, values=["Easy", "Normal", "Expert"]))
        self.label.config(text="Guess a number")

        self.entry.config(
            validate="key",
            validatecommand="self.validate_input(self.entry.get())"
        )  # Direct validation
        self.button.config()
        self.label2.config(text="Guess from 1 to 10")
        self.difficulty_combo.set("Easy")

        self.label.pack(side="top", fill="both")
        self.entry.pack(side="top", fill="both")
        self.button.pack(side="top", fill="both")
        self.label2.pack(side="top", fill="both")
        self.label3.pack(side="top", fill="both")
        self.difficulty_combo.pack(side="top", fill="both")

    def validate_input(self, entry_input: str):
        """
        Validate user input on every key press.

        Parameters:
            self:
            entry_input: Input from text entry.

        Returns:
              None
        """
        if entry_input.isdigit() or entry_input == "":
            self.label2.config(text="")  # Clear previous feedback
            return
        else:
            self.label2.config(
                text="Invalid Input. Enter a number from 1 to 10."
            )
            return

    def generate_and_compare(self, low: int, high: int) -> None:
        """
        Generate and compare guesses, when button is hit

        Parameters:
            self:
            low: lowest integer of guessing range
            high: highest integer of guessing range

        Returns:
            None
        """
        random_integer: int = random.randint(low, high)
        self.counter += 1
        try:
            guess: int = int(self.entry.get())
            if random_integer == guess:
                self.label2.config(text="Guess is correct!")
            else:
                self.label2.config(
                    text=f"Guess again. The number was {random_integer}.")
            self.entry.delete(0, tk.END)
        except (ValueError, TypeError):
            self.label2.config(
                text="Invalid Input. Enter a number from 1 to 10."
            )

        self.label3.config(text=f"You made {self.counter} number of guesses")

    def levels(self):
        """
        used to define levels and manage level selection

        Parameters:

            self:

        Returns:
        """
        self.combo_value = self.difficulty_combo.get()
        match self.combo_value:
            case "Easy":
                self.generate_and_compare(1, 10)
            case "Normal":
                self.generate_and_compare(1, 100)
            case "Expert":
                self.generate_and_compare(1, 1000)


def main() -> None:
    """
    Main function to orchestrate program flow

    Parameters:


    Returns:
        None
    """
    try:
        root = tk.Tk()
        root.title("Number Guessing Game")
        root.geometry("1024x768")
        MainApplication(root).pack(side="top", fill="both", expand=True)

        root.mainloop()
    except Exception as e:
        tkinter.messagebox.showerror(f'Error has occurred {e}')


if __name__ == "__main__":
    main()
