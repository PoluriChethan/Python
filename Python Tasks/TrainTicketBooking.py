# CONFIGURATION
TOTAL_CAPACITY = 2

# Initialization
seats = {i: "Available" for i in range(1, TOTAL_CAPACITY + 1)}
waiting_list = []

while True:
    # 1. Show Current Status
    print(f"\n{'='*10} TRAIN DASHBOARD {'='*10}")
    for s_num, status in seats.items():
        print(f"Seat {s_num}: {status}")
    
    print("-" * 34)
    if waiting_list:
        for i in range(len(waiting_list)):
            print(f"WL {i+1}: {waiting_list[i]}")
    else:
        print("Waiting List: Empty")
    print("=" * 34)

    # 2. Ask for the number of seats
    request = input("\nHow many seats to book? (or 'exit'): ")
    if request.lower() == 'exit':
        break
    
    num_to_book = int(request)
    current_booking_results = [] # Temporary list to store results for this batch

    # 3. Process each passenger entry
    for i in range(num_to_book):
        p_name = input(f"Enter name for passenger {i+1}: ")
        
        booked = False
        # Check for Available Seats
        for s_num in seats:
            if seats[s_num] == "Available":
                seats[s_num] = p_name
                current_booking_results.append(f"CONFIRMED: {p_name} (Seat {s_num})")
                booked = True
                break
        
        # Check Waiting List if Seats are Full
        if not booked:
            if len(waiting_list) < TOTAL_CAPACITY:
                waiting_list.append(p_name)
                current_booking_results.append(f"WAITING: {p_name} (WL{len(waiting_list)})")
            else:
                current_booking_results.append(f"REJECTED: {p_name} (No seat left)")

    # 4. SHOW RESULTS ONLY AFTER ALL NAMES ARE ENTERED
    print("\n--- BOOKING SUMMARY ---")
    for result in current_booking_results:
        print(result)
    print("-----------------------")

print("Program Closed.")
