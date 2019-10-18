nic_list = [123, 234, 456, 457, 122]
delete_nic = 456

nic_list = [nic for nic in nic_list if nic != delete_nic]

delete_customer_id = 23

# customer_list = [customer for customer in customer_list if delete_customer_id != customer.id]


x_values = [1, 2, 3, 4]
y_values = [x ** 2 for x in x_values if x != 3]