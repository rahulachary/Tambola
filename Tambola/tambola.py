import random

players = {
    "Player 1": {"numbers": random.sample(range(1, 91), 10), "matched": []},
    "Player 2": {"numbers": random.sample(range(1, 91), 10), "matched": []},
    "Player 3": {"numbers": random.sample(range(1, 91), 10), "matched": []}
}

print(" Players and their assigned numbers:\n")
for name in players:
    print(name, ":", sorted(players[name]["numbers"]))

caller_numbers = list(range(1, 91))
random.shuffle(caller_numbers)

print("\n Tambola Game Started \n")

for number in caller_numbers:
    input("Press Enter to call next number...")
    print(" Number Called:", number)

    for name in players:
        if number in players[name]["numbers"] and number not in players[name]["matched"]:
            players[name]["matched"].append(number)
            print(name,"matched",number) 
            print("Total matched: ",{len(players[name]['matched'])})


            if len(players[name]["matched"]) == 5:
                print("\n",name, "WINS-By early 5")
                exit()

    print("-" * 40)
