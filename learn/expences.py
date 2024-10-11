from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ExpenseTrackerApp(App):
    def build(self):
        self.title = "Expense Tracker"
        return ExpenseLayout()

class ExpenseLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # UI elements
        self.item_input = TextInput(hint_text="Item name")
        self.amount_input = TextInput(hint_text="Amount")
        self.date_input = TextInput(hint_text="Date (YYYY-MM-DD)")
        self.comment_input = TextInput(hint_text="Comment")
        self.add_button = Button(text="Add Expense", on_press=self.add_expense)
        self.expense_list = Label()

        # Add UI elements to layout
        self.add_widget(self.item_input)
        self.add_widget(self.amount_input)
        self.add_widget(self.date_input)
        self.add_widget(self.comment_input)
        self.add_widget(self.add_button)
        self.add_widget(self.expense_list)

        # Expense data
        self.expenses = []

    def add_expense(self, instance):
        item_name = self.item_input.text
        amount = self.amount_input.text
        date = self.date_input.text
        comment = self.comment_input.text

        self.expenses.append(f"{item_name} | ${amount} | {date} | {comment}")
        self.update_expense_list()

    def update_expense_list(self):
        self.expense_list.text = "\n".join(self.expenses)

if __name__ == "__main__":
    ExpenseTrackerApp().run()
