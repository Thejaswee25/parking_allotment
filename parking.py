import datetime
import time

class ParkingLot:
    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.parking_spots = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
        self.available_spots = num_rows * num_cols
        self.vehicle_info = {}

    def display_parking_lot(self):
        print("|-------------------|")
        for row in range(self.num_rows):
            print("|", end='')
            for col in range(self.num_cols):
                spot = self.parking_spots[row][col]
                if spot != ' ':
                    vehicle = self.vehicle_info[spot]
                    display_text = f"{vehicle['type'][0]}({spot})"
                    print(f"[{display_text: <10}]", end='')
                else:
                    print("[          ]", end='')
            print("|")
        print("|-------------------|")

    def add_vehicle(self, vehicle_type, plate_number, row, col):
        if self.parking_spots[row][col] == ' ' and plate_number not in self.vehicle_info:
            self.parking_spots[row][col] = plate_number
            self.available_spots -= 1
            entry_time = datetime.datetime.now()
            self.vehicle_info[plate_number] = {
                "type": vehicle_type,
                "entry_time": entry_time,
                "position": (row, col)
            }
            print("Vehicle Added to Lot!")
            print("Time Entered:", entry_time.strftime("%H:%M:%S"))
            print("SPOTS AVAILABLE:", self.available_spots)
            time.sleep(2)
        else:
            if plate_number in self.vehicle_info:
                print("Duplicate plate number. Vehicle cannot be added.")
            else:
                print("Spot is already occupied.")

    def remove_vehicle(self, row, col):
        if self.parking_spots[row][col] != ' ':
            plate_number = self.parking_spots[row][col]
            if plate_number in self.vehicle_info:
                exit_time = datetime.datetime.now()
                entry_time = self.vehicle_info[plate_number]["entry_time"]
                elapsed_time = exit_time - entry_time
                hours_parked = elapsed_time.total_seconds() / 3600
                fare = calculate_fare(hours_parked)
                print("Vehicle Removed from Lot!")
                print("Time Exited:", exit_time.strftime("%H:%M:%S"))
                print("Fare: Rs.", fare)
                print("SPOTS AVAILABLE:", self.available_spots + 1)
                del self.vehicle_info[plate_number]
                self.parking_spots[row][col] = ' '
                self.available_spots += 1
            else:
                print("No vehicle parked in that spot.")
        else:
            print("No vehicle parked in that spot.")

    def view_vehicle_info(self, row, col):
        if self.parking_spots[row][col] != ' ':
            plate_number = self.parking_spots[row][col]
            if plate_number in self.vehicle_info:
                vehicle_type = self.vehicle_info[plate_number]["type"]
                entry_time = self.vehicle_info[plate_number]["entry_time"]
                print("Vehicle Type:", vehicle_type)
                print("Plate Number:", plate_number)
                print("Entry Time:", entry_time.strftime("%H:%M:%S"))
            else:
                print("No vehicle parked in that spot.")
        else:
            print("No vehicle parked in that spot.")

    def view_vehicle_by_plate(self, plate_number):
        if plate_number in self.vehicle_info:
            vehicle_type = self.vehicle_info[plate_number]["type"]
            entry_time = self.vehicle_info[plate_number]["entry_time"]
            row, col = self.vehicle_info[plate_number]["position"]
            print("Vehicle Found!")
            print("Vehicle Type:", vehicle_type)
            print("Plate Number:", plate_number)
            print("Entry Time:", entry_time.strftime("%H:%M:%S"))
            print(f"Parked at Row: {row}, Column: {col}")
        else:
            print(f"No vehicle with plate number '{plate_number}' found.")

def calculate_fare(hours_parked):
    base_rate = 400.0
    hourly_rate = 100.0
    fare = base_rate + (hours_parked * hourly_rate)
    return round(fare, 2)

def main():
    num_rows = 10
    num_cols = 10
    parking_lot = ParkingLot(num_rows, num_cols)
    while True:
        print("1. Add Vehicle")
        print("2. Remove Vehicle")
        print("3. View Vehicle Info by Spot")
        print("4. View Vehicle Info by Plate Number")
        print("5. Display Parking Lot")
        print("6. Exit")
        choice = int(input(">"))
        if choice == 1:
            print("Enter Vehicle Type:")
            print("1. Car")
            print("2. Truck")
            print("3. Motorcycle")
            vehicle_type_input = int(input(">"))
            vehicle_types = {1: "Car", 2: "Truck", 3: "Motorcycle"}
            vehicle_type = vehicle_types.get(vehicle_type_input, None)
            if vehicle_type is None:
                print("Invalid vehicle type.")
                continue
            parking_lot.display_parking_lot()
            print("SPOTS AVAILABLE:", parking_lot.available_spots)
            plate_number = input("Enter New Vehicle Plate Number:\n>")
            row = int(input("Select Row to Park In:\n>"))
            col = int(input("Select Space to Park In:\n>"))
            parking_lot.add_vehicle(vehicle_type, plate_number, row, col)
        elif choice == 2:
            parking_lot.display_parking_lot()
            print("SPOTS AVAILABLE:", parking_lot.available_spots)
            row = int(input("Select Row to Remove Vehicle From:\n>"))
            col = int(input("Select Space to Remove Vehicle From:\n>"))
            parking_lot.remove_vehicle(row, col)
        elif choice == 3:
            parking_lot.display_parking_lot()
            print("SPOTS AVAILABLE:", parking_lot.available_spots)
            row = int(input("Select Row to View Vehicle Info:\n>"))
            col = int(input("Select Space to View Vehicle Info:\n>"))
            parking_lot.view_vehicle_info(row, col)
        elif choice == 4:
            plate_number = input("Enter Vehicle Plate Number to Search:\n>")
            parking_lot.view_vehicle_by_plate(plate_number)
        elif choice == 5:
            parking_lot.display_parking_lot()
            print("SPOTS AVAILABLE:", parking_lot.available_spots)
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
