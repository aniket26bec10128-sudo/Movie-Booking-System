movies = ["doomsday", "spidermanbrandnewday", "secertwars"]
prices = [190, 250, 300]
bookings = []

def show_movies():
    for i in range(len(movies)):
        print(i + 1, movies[i], "- Rs.", prices[i])

def book_ticket():
    show_movies()

    m = int(input("Enter movie number: "))

    if m >= 1 and m <= 3:
        print("1. 09:00 AM")
        print("2. 1:45 PM")
        print("3. 6:00 PM")

        s = int(input("Enter show number: "))
        t = int(input("Enter number of tickets: "))

        if s >= 1 and s <= 3 and t > 0:
            amount = prices[m - 1] * t

            bookings.append([movies[m - 1], s, t, amount])

            print("\nBooking Confirmed!")
            print("Movie:", movies[m - 1])
            print("Tickets:", t)
            print("Amount: Rs.", amount)
        else:
            print("Invalid input!")
    else:
        print("Invalid movie number!")

while True:
    print("\n--- MOVIE TICKET BOOKING ---")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        show_movies()

    elif choice == 2:
        book_ticket()

    elif choice == 3:
        for i in range(len(bookings)):
            print(i + 1, bookings[i])

    elif choice == 4:
        break

    else:
        print("Invalid choice!")