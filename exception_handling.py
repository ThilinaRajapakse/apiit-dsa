def find_customer(customer_list, customer_id):
    first = 0
    last = len(customer_list) - 1
    
    while (first != last):
        mid = (first + last) // 2
        if customer_list[mid].id == customer_id:
            customer_list[mid] = update_customer_details(customer_list[mid])
            print("Customer updated.")
            return True
        else:
            if customer_id < customer_list[mid].id:
                last = mid
            else:
                first = mid
    if customer_list[first].id == customer_id:
        customer_list[first] = update_customer_details(customer_list[first])
        print("Customer updated.")
        return True
    else:
        raise ValueError("Customer not found.")


def update_customer_details(customer):
    customer.name = input("ENter new name: ")
    # Update details

    return customer
    



while True:
    try:
        choice = int(input("Enter choice: "))

        if choice == 0:
            pass
        elif choice == 1:
            pass
        else:
            raise ValueError("Invalid choice.")
    except ValueError:
        print("Invalid choice. Please select an available option.")
        continue
