import random
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


class MainApplication(tk.Frame):
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
        self.label = Label(self)
        self.label2 = Label(self)
        self.entry = Entry(self)
        self.button = Button(self, text="Submit", command=self.genandcomp)

        self.label.config(text="Guess a number")

        self.entry.config(validate="key", validatecommand="self.validate_input(self.entry.get())")  # Direct validation
        self.button.config()
        self.label2.config(text="Guess from 1 to 10")

        self.label.pack(side="top", fill="both")
        self.entry.pack(side="top", fill="both")
        self.button.pack(side="top", fill="both")
        self.label2.pack(side="top", fill="both")

    def validate_input(self, input):
        """
        Validate user input on every key press.

        Parameters:
            self:
            input: Input from text entry.

        Returns:
              None
        """
        if input.isdigit() or input == "":  # Allow empty input for clearing
            self.label2.config(text="")  # Clear previous feedback
            return
        else:
            self.label2.config(text="Invalid Input. Enter a number from 1 to 10.")
            return

    def genandcomp(self) -> None:
        """
        Generate and compare guesses, when button is hit

        Parameters:
            self:

        Returns:
            None
        """
        randomint: int = random.randint(1, 10)
        try:
            guess: int = int(self.entry.get())
            if randomint == guess:
                self.label2.config(text="Guess is correct!")
            else:
                self.label2.config(
                    text=f"Guess again. The number was {randomint}.")
            self.entry.delete(0, tk.END)
        except (ValueError, TypeError):
            self.label2.config(text="Invalid Input. Enter a number from 1 to 10.")

def main() -> None:
    """
    Main function to orchestrate program flow

    Parameters:
        None

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
        messagebox.showerror(f'Error has occurred {e}')


if __name__ == "__main__":
    main()