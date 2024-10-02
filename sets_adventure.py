
def route_compare(ours_routes,competitors_routes,operation):
    if operation.lower() == 'intersection':
        result = ours_routes.intersection(competitors_routes)
        print(result)
    elif operation.lower() == 'difference':
        result = ours_routes.difference(competitors_routes)
        print(result)
    elif operation.lower() == 'symmetric_difference':
        result = ours_routes.symmetric_difference(competitors_routes)
        print(result)
    else:
        print("Invalid operation")

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True:
    print(f"\n Please select an option...")
    print(" 1. Compare Routes")
    print(" 2. Exit")

    choice = int(input(f"\n Please enter a number 1-2 for the option you woud like: "))
    if choice == 1:
        select_operation = input(f"\n Please select an operation ( intersection, difference, symmetric_difference):  ")
        route_compare(our_routes,competitor_routes,select_operation)
    elif choice == 2:
        break
    else:
        print(f"\n Invalid choice! Please try again")


