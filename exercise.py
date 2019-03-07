seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey", "Toast", "Pacha", "Mau"]
]


for row_num, col in enumerate(seats):
    for seat_num, seat in enumerate(col):
        if seat is None:
            print("Row {} seat {} is free. Do you want to sit there? (y/n) ".format(row_num + 1, seat_num + 1))
            user_ans = input().lower()
            if user_ans == "y":
                user_name = input("What is your name? ")
                seats[row_num].remove(seat)
                seats[row_num].insert(seat_num, user_name)
                print(seats)
                quit()
