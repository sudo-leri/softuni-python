days = int(input())
players = int(input())
energy = float(input())
water_day_one_player = float(input())
food_day_one_player = float(input())

water = water_day_one_player * players * days
food = food_day_one_player * players * days

for day in range(1, days + 1):
    energy_lost = float(input())
    energy -= energy_lost

    if day % 2 == 0:
        energy += energy * 5/100
        water -= water * 30/100

    if day % 3 == 0:
        food -= food / players
        energy += energy * 10/100

    if energy <= 0:
        print(f"You will run out of energy. You will be left with {food:.2f} food and {water:.2f} water.")
    elif day == days:
        print(f"You are ready for the quest. You will be left with - {energy:.2f} energy!")
