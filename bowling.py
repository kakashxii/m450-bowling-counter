def print_pins(num_pins):
    pins = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
    knocked_pins = 10 - num_pins

    if knocked_pins > 0:
        for i in range(knocked_pins):
            pins[i] = '░░'

    print("          1         ")
    print("         2 3        ")
    print("        4 5 6       ")
    print("       7 8 9 10     ")
    print("___________________")
    print("|" + pins[6] + "|" + pins[7] + "|" + pins[8] + "|" + pins[9] + "|")
    print("| |" + pins[4] + "|" + pins[5] + "|" + pins[3] + "| |")
    print("| | |" + pins[2] + "|" + pins[1] + "| | |")
    print("| | | |" + pins[0] + "| | | |")
    print("|_|_|_|_|_|_|_|_|_|")
    print("\n")


def bowling_counter():
    score = 0
    frame = 1

    while frame <= 10:
        print(f"Frame {frame}")
        first_throw = int(input("Enter the pins overturned in the first throw: "))

        if first_throw > 10 or first_throw < 0:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue

        print_pins(first_throw)

        if first_throw == 10 and frame < 10:
            print("Strike!")
            score += 10
            frame += 1
            continue
        elif first_throw == 10 and frame == 10:
            print("Strike!")
            score += 10

            # Second throw in 10th frame
            second_throw = int(input("Enter the pins overturned in the second throw: "))
            print_pins(second_throw)
            score += second_throw

            if second_throw == 10:  # Player gets two additional throws
                print("Strike!")
                score += 10

                # Third throw in 10th frame
                third_throw = int(input("Enter the pins overturned in the third throw: "))
                print_pins(third_throw)
                score += third_throw

            frame += 1
            continue
        elif first_throw == 0:
            print('Miss!')

        second_throw = int(input("Enter the pins overturned in the second throw: "))

        if second_throw > 10 or second_throw < 0 or (first_throw + second_throw) > 10:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue

        print_pins(second_throw)
        frame_score = first_throw + second_throw
        score += frame_score

        if frame_score == 10:  # Spare
            print("Spare!")
            if frame == 10:
                # Bonus throw for spare in 10th frame
                bonus_throw = int(input("Enter the pins overturned in the bonus throw: "))
                print_pins(bonus_throw)
                score += bonus_throw
        elif frame_score == first_throw:
            print('Miss!')

        elif frame_score < 10:
            print("Open Frame!")

        frame += 1
    
    if score == 130:
        print('Perfect game!')
        score = 300
    print(f"Total score: {score}")


ascii_art = """


██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░██╗███╗░░██╗░██████╗░░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
██████╦╝██║░░██║░╚██╗████╗██╔╝██║░░░░░██║██╔██╗██║██║░░██╗██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
██╔══██╗██║░░██║░░████╔═████║░██║░░░░░██║██║╚████║██║░░╚██╗██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║██║░╚███║╚██████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

"""

print(ascii_art)
bowling_counter()
