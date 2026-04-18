class House:
    def __init__(self, house_number, door_colour):
        self.house_number = house_number
        self.door_colour = door_colour
        self.number_of_floors = 2

    def get_details(self):
        return f"House number {self.house_number} has {self.number_of_floors} floors and a {self.door_colour} door."

    def repaint_door(self, colour):
        self.door_colour = colour






