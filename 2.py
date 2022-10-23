input_vehicles = input()
vehicles = input_vehicles.split('>>')
total_tax = 0

for vehicle in vehicles:
    vehicle = vehicle.split(' ')
    type_vehicle = vehicle[0]
    years = int(vehicle[1])
    kilometers = int(vehicle[2])

    if type_vehicle != 'family' and type_vehicle != 'heavyDuty' and type_vehicle != 'sports':
        print('Invalid car type.')

    elif type_vehicle == 'family':
        tax_kilometers_times = int(kilometers / 3000)
        tax_kilometers = tax_kilometers_times * 12

        tax_year = years * 5

        tax = 50 + tax_kilometers - tax_year
        total_tax += tax

        print(f"A {type_vehicle} car will pay {tax:.2f} euros in taxes.")

    elif type_vehicle == 'heavyDuty':
        tax_kilometers_times = int(kilometers / 9000)
        tax_kilometers = tax_kilometers_times * 14

        tax_year = years * 8

        tax = 80 + tax_kilometers - tax_year
        total_tax += tax

        print(f"A {type_vehicle} car will pay {tax:.2f} euros in taxes.")

    elif type_vehicle == 'sports':
        tax_kilometers_times = int(kilometers / 2000)
        tax_kilometers = tax_kilometers_times * 18

        tax_year = years * 9

        tax = 100 + tax_kilometers - tax_year
        total_tax += tax

        print(f"A {type_vehicle} car will pay {tax:.2f} euros in taxes.")

print(f'The National Revenue Agency will collect {total_tax:.2f} euros in taxes.')
