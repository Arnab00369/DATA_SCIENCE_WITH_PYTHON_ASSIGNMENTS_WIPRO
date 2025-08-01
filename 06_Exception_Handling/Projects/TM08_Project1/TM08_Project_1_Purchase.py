# Project 1:

def process_purchase_file():
   try:
      filename = input("Enter the file name: ")
      with open(filename + ".txt", 'r') as file:
            lines = file.readlines()

      purchased_items = 0
      free_items = 0
      total_amount = 0
      discount = 0

      for line in lines:
            line = line.strip()
            if not line:
               continue  # Skip blank lines
            parts = line.split()
            if len(parts) == 2:
               item, price = parts[0], parts[1]
               if item.lower() == 'discount':
                  try:
                        discount = int(price)
                  except ValueError:
                        print(f"Invalid discount value: {price}")
                        discount = 0
               elif price.lower() == 'free':
                  free_items += 1
               else:
                  try:
                        total_amount += int(price)
                        purchased_items += 1
                  except ValueError:
                        print(f"Invalid price for item {item}: {price}")
            else:
               print(f"Invalid line format: {line}")

      final_amount = total_amount - discount

      print("\nNo of items purchased:", purchased_items)
      print("No of free items:", free_items)
      print("Amount to pay:", total_amount)
      print("Discount given:", discount)
      print("Final amount paid:", final_amount)

   except FileNotFoundError:
      print("Error: File not found.")
   except Exception as e:
      print("An unexpected error occurred:", str(e))


# Run the function
process_purchase_file()
