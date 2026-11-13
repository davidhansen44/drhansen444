from csv import reader
from datetime import datetime


def read_dictionary(filename, key_column_index):

    products = {}

    with open(filename, "rt") as csv_file:
        csv_reader = reader(csv_file)

     
        next(csv_reader)

        for row in csv_reader:
            key = row[key_column_index]
            products[key] = row

    return products


def main():
    try:
      
        products = read_dictionary("products.csv", 0)

        print("=" * 40)
        print("      Hansen Grocery Store")
        print("=" * 40)

        subtotal = 0
        total_items = 0

        with open("request.csv", "rt") as request_file:
            
            csv_reader = reader(request_file)

           
            next(csv_reader)

            print("Items Purchased:")

            for row in csv_reader:
                product_number = row[0]
                quantity = int(row[1])

                product = products[product_number]

                product_name = product[1]
                price = float(product[2])

                line_total = quantity * price

                subtotal += line_total
                total_items += quantity

                print(f"{product_name}: {quantity} @ ${price:.2f}")

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(" " + "-" * 40)
        print(f"Number of Items: {total_items}")
        print(f"Subtotal:        ${subtotal:.2f}")
        print(f"Sales Tax:       ${sales_tax:.2f}")
        print(f"Total:           ${total:.2f}")
        print("-" * 40)

        print("Thank you for shopping at the Hansen Grocery Store!")

        current_date = datetime.now()

        print(current_date.strftime("%A %b %d, %Y %I:%M %p"))

    except FileNotFoundError:

        print("Error: one of the files could not be found.")

    except PermissionError:

        print("Error: permission denied while accessing a file.")

    except KeyError as error:

        print(f"Error: unknown product ID in request file: {error}")


if __name__ == "__main__":
    main()