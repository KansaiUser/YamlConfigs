from car_data import car_data

def calculate_volume(length, width, height):
    return length * width * height

def calculate_average_fuel_efficiency(fuel_efficiency):
    return sum(fuel_efficiency) / len(fuel_efficiency)

def main():
    total_volume = 0
    for car in car_data:
        model = car["model"]
        length = car["length"]
        width = car["width"]
        height = car["height"]
        fuel_efficiency = car["fuel_efficiency"]

        # Calculate the volume for the current car
        volume = calculate_volume(length, width, height)
        print(f"The volume of {model} is {volume:.2f} cubic meters.")
        
        # Add to the total volume
        total_volume += volume

        # Calculate the average fuel efficiency
        avg_fuel_efficiency = calculate_average_fuel_efficiency(fuel_efficiency)
        print(f"The average fuel efficiency of {model} is {avg_fuel_efficiency:.2f} km/l.")

    # Calculate the average volume across all cars
    average_volume = total_volume / len(car_data)
    print(f"\nThe average volume of the cars is {average_volume:.2f} cubic meters.")

if __name__ == "__main__":
    main()
