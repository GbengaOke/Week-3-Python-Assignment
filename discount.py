#ASSIGNMENT 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price*(discount_percent/100))
        return final_price
    else:
        return price
 
# Example usage:
original_price = 100.0
discount_percent = 25


final_price = calculate_discount(original_price, discount_percent)

print(f"Final Price (after discount) is: {final_price}")




#ASSIGNMENT 2
# Define the function to calculate the discount
def calculate_discount(original_price, discount_percentage):
    if discount_percentage > 0:
        discount_amount = original_price * (discount_percentage / 100)
        final_price = original_price - discount_amount
        return final_price
    else:
        return original_price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if discount_percentage > 0:
    print(f"Final Price (after discount) is: {final_price} ")
else:
    print(f"Final price (No discount applied) is: {original_price:.2f}")
