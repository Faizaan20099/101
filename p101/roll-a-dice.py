import random

# Initialize response to 'y'
response = "y"

# Use a while loop to keep rolling the dice while response is 'y'
while response.lower() == "y":
    # Generate a random number between 1 and 6
    dice_number = random.randint(1, 6)
    
    # Print the dice face corresponding to the random number
    if dice_number == 1:
        print("[-----]")
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
        print("[-----]")
    elif dice_number == 2:
        print("[-----]")
        print("[*    ]")
        print("[     ]")
        print("[    *]")
        print("[-----]")
    elif dice_number == 3:
        print("[-----]")
        print("[*    ]")
        print("[  *  ]")
        print("[    *]")
        print("[-----]")
    elif dice_number == 4:
        print("[-----]")
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
        print("[-----]")
    elif dice_number == 5:
        print("[-----]")
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
        print("[-----]")
    elif dice_number == 6:
        print("[-----]")
        print("[*   *]")
        print("[*   *]")
        print("[*   *]")
        print("[-----]")
    
    # Prompt the user to continue or exit
    response = input("Do you want to roll the dice again? (y/n): ")
