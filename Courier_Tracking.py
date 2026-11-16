
# COURIER TRACKING SYSTEM

# 1. List of parcel statuses
statuses = ["Booked", "Picked Up", "In Transit",
            "Out for Delivery", "Delivered"]


# 2. Dictionary to store parcel details
# CT1002 is already Delivered as required in Test Case 3(b)

parcels = {
    "CT1002": {
        "sender": "Test Sender",
        "receiver": "Test Receiver",
        "destination": "Raipur",
        "status": "Delivered",
        "history": ["Booked", "Picked Up", "In Transit",
                    "Out for Delivery", "Delivered"]
    }
}


# 3. Starting number for tracking ID
next_id = 1001


# 4. Function to book a parcel
def book_parcel():

    global next_id

    sender = input("Enter sender name: ")
    receiver = input("Enter receiver name: ")
    destination = input("Enter destination: ")

    # Generate a unique tracking ID
    while "CT" + str(next_id) in parcels:
        next_id += 1

    tracking_id = "CT" + str(next_id)
    next_id += 1

    # Store parcel details in dictionary
    parcels[tracking_id] = {
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "status": "Booked",
        "history": ["Booked"]
    }

    print("Parcel booked. Tracking ID:", tracking_id,
          "| Status: Booked")


# 5. Function to update parcel status
def update_status():

    tracking_id = input("Enter tracking ID: ").strip().upper()

    # Check whether tracking ID exists
    if tracking_id not in parcels:
        print("Tracking ID", tracking_id, "not found.")
        return

    parcel = parcels[tracking_id]

    # Check whether parcel is already delivered
    if parcel["status"] == "Delivered":
        print("Parcel", tracking_id,
              "is already delivered. No further updates allowed.")
        return

    # Find current status position
    current_index = statuses.index(parcel["status"])

    # Get next status
    new_status = statuses[current_index + 1]

    # Update parcel status
    old_status = parcel["status"]
    parcel["status"] = new_status

    # Add new status to history
    parcel["history"].append(new_status)

    print("Status updated:", old_status, "->", new_status)


# 6. Function to track a parcel
def track_parcel():

    tracking_id = input("Enter tracking ID: ").strip().upper()

    # Check whether tracking ID exists
    if tracking_id not in parcels:
        print("Tracking ID", tracking_id, "not found.")
        return

    parcel = parcels[tracking_id]

    # Display parcel information
    print("Tracking ID:", tracking_id,
          "| Receiver:", parcel["receiver"],
          "| Destination:", parcel["destination"])

    # Display complete status history
    print("History:", " -> ".join(parcel["history"]))

    # Display current status
    print("Current status:", parcel["status"])


# 7. Function to search parcel by receiver name
def search_receiver():

    name = input("Enter receiver name: ").strip()

    found = False

    # Search through all parcels
    for tracking_id, parcel in parcels.items():

        if parcel["receiver"].lower() == name.lower():

            print("\nParcel Found!")
            print("Tracking ID:", tracking_id)
            print("Receiver:", parcel["receiver"])
            print("Destination:", parcel["destination"])
            print("Current Status:", parcel["status"])

            found = True

    # If receiver is not found
    if found == False:
        print("No parcel found for this receiver.")


# 8. Main menu
while True:

    print("\n===== COURIER TRACKING SYSTEM =====")
    print("1. Book Parcel")
    print("2. Update Status")
    print("3. Track Parcel")
    print("4. Search by Receiver")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_parcel()

    elif choice == "2":
        update_status()

    elif choice == "3":
        track_parcel()

    elif choice == "4":
        search_receiver()

    elif choice == "5":
        print("Thank you for using Courier Tracking System!")
        break

    else:
        print("Invalid choice! Please try again.")
