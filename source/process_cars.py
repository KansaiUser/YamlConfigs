import hydra
from omegaconf import DictConfig
from pathlib import Path


def calculate_volume(length, width, height):
    return length * width * height

def calculate_average_fuel_efficiency(fuel_efficiency):
    return sum(fuel_efficiency) / len(fuel_efficiency)

@hydra.main(config_path="config", config_name="car_data", version_base=None)
def main(cfg:DictConfig):
    total_volume = 0
    for car in cfg.cars:
        model = car.model
        length = car.length
        width = car.width
        height = car.height
        fuel_efficiency = car.fuel_efficiency

        # Calculate the volume for the current car
        volume = calculate_volume(length, width, height)
        print(f"The volume of {model} is {volume:.2f} cubic meters.")
        
        # Add to the total volume
        total_volume += volume

        # Calculate the average fuel efficiency
        avg_fuel_efficiency = calculate_average_fuel_efficiency(fuel_efficiency)
        print(f"The average fuel efficiency of {model} is {avg_fuel_efficiency:.2f} km/l.")

    # Calculate the average volume across all cars
    average_volume = total_volume / len(cfg.cars)
    print(f"\nThe average volume of the cars is {average_volume:.2f} cubic meters.")

if __name__ == "__main__":
    main()
