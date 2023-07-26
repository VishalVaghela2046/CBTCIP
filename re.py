def generate_payment_receipt(customer_name, payment_date, payment_amount, payment_method):
    receipt_template = """
    ------------------------------
            PAYMENT RECEIPT
    ------------------------------
    
    Customer Name: {customer_name}
    Payment Date : {payment_date}
    Amount       : ${payment_amount:.2f}
    Payment Method: {payment_method}
    
    ------------------------------
                Thank You!
    ------------------------------
    """

    receipt = receipt_template.format(
        customer_name=customer_name,
        payment_date=payment_date,
        payment_amount=payment_amount,
        payment_method=payment_method
    )

    return receipt

# Example usage
customer_name = "John Doe"
payment_date = "2023-07-26"
payment_amount = 500.00
payment_method = "Credit Card"

receipt = generate_payment_receipt(customer_name, payment_date, payment_amount, payment_method)
print(receipt)
