import tkinter as tk
from tkinter import ttk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Email Detection")
        self.root.geometry("600x400")

        self.label = tk.Label(
            root,
            text="Spam email detection using machine learning",
            font=("Helvetica", 15),
        )
        self.label.pack(padx=20, pady=20)

        self.label_email = tk.Label(root, text="Enter your email:")
        self.label_email.pack(padx=20, pady=5)

        self.email_entry = tk.Entry(
            root,
            width=40,
            font=("Helvetica", 12),
            justify="center",
            show="",
            insertbackground="black",
            relief="solid",
            bd=1,
        )

        self.email_entry.insert(0, "")
        self.email_entry.pack(pady=10)

        self.options = ttk.Combobox(
            root,
            values=[
                "Decision Tree",
                "Logistic Regression",
                "Naive",
                "Random Forest",
                "svm",
            ],
        )
        self.options.set("Decision Tree")
        self.options.pack(pady=10)

        self.start_button = tk.Button(
            root, text="Start", command=self.on_start_button_click
        )
        self.start_button.pack(pady=10)

    def on_start_button_click(self):
        entered_email = self.email_entry.get()
        selected_option = self.options.get()
        print(f"Entered Email: {entered_email}")
        print(f"Selected Option: {selected_option}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
