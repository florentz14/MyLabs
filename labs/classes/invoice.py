from tabulate import tabulate

class InvoiceDetails:
    def __init__(self, invoice_number, customer_name, amount_due, tax_rate=0.07, discount=0.0):
        self.invoice_number = invoice_number
        self.customer_name = customer_name
        self.amount_due = amount_due
        self.tax_rate = tax_rate
        self.discount = discount

    def display_invoice(self):
        print(f"Invoice Number: {self.invoice_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Amount Due: ${self.amount_due:.2f}")
        print(f"Tax Rate: {self.tax_rate:.2%}")
        print(f"Discount: {self.discount:.2%}")

    def calculate_total(self):
        tax_amount = self.amount_due * self.tax_rate
        discount_amount = self.amount_due * self.discount
        total = self.amount_due + tax_amount - discount_amount
        return total
    
    def additional_info(self, info: str):
        print(f"Additional Info: {info}")

    def apply_discount(self, discount_rate: float):
        self.discount = discount_rate
        print(f"Applied discount of {discount_rate:.2%} to invoice {self.invoice_number}")

    def add_item(self, item_name: str, item_price: float):
        self.amount_due += item_price
        print(f"Added item '{item_name}' with price ${item_price:.2f} to invoice {self.invoice_number}")        
    
    def display_invoice_details(self):
        total = self.calculate_total()
        table = [
            ["Invoice Number", self.invoice_number],
            ["Customer Name", self.customer_name],
            ["Amount Due", f"${self.amount_due:.2f}"],
            ["Tax Rate", f"{self.tax_rate:.2%}"],
            ["Discount", f"{self.discount:.2%}"],
            ["Total Amount", f"${total:.2f}"]
        ]
        print(tabulate(table, headers=["Description", "Value"], tablefmt="grid"))   


class Invoice:
    def __init__(self, invoice_details: InvoiceDetails):
        self.invoice_details = invoice_details

    def generate_invoice(self):
        print("Generating Invoice...")
        self.invoice_details.display_invoice()        