from pydantic import BaseModel, conlist, ValidationError, Field
from strictyaml import YAML, load,YAMLError
# import strictyaml as sy
from typing import Optional, Annotated
from pathlib import Path

# Define a Pydantic model for car data
class CarData(BaseModel):
    model: str
    length: float
    width: float
    height: float
    # fuel_efficiency: list[float] = Field(min_length=3, max_length=3)
    # fuel_efficiency: conlist(float, min_length=3, max_length=3)
    fuel_efficiency: Annotated[list[float], Field(min_length=3, max_length=3)]

class CarsData(BaseModel):
    listCar : list[CarData]


def load_car_data(filename:Path="car_data.yaml") -> YAML:
    with open(filename, "r") as file:
        try:
            yaml_data = load(file.read())
            return yaml_data    
        except YAMLError as e:
            print(f"Error parsing YAML file: {e}")
        except ValidationError as e:
            print(f"Data validation error: {e}")

def validate_config(parsed_config: YAML=None) -> Optional[CarsData]:
    if parsed_config is None:
        print("Parsed config is None")
        return None

    try:
        # Convert YAML data into CarsData model
        car_list_data = [CarData(**item) for item in parsed_config.data]
        return CarsData(listCar=car_list_data)
    except ValidationError as e:
        print(f"Data validation error: {e}")
        return None

def calculate_volume(length, width, height):
    return length * width * height

def calculate_average_fuel_efficiency(fuel_efficiency):
    return sum(fuel_efficiency) / len(fuel_efficiency)

def main():
    car_data = validate_config(load_car_data())
    
    if car_data is None:
        return

    total_volume = 0
    for car in car_data.listCar:
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
    average_volume = total_volume / len(car_data.listCar)
    print(f"\nThe average volume of the cars is {average_volume:.2f} cubic meters.")

if __name__ == "__main__":
    main()
