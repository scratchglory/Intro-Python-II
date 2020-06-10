# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, desc1, desc2):
        self.desc1 = desc1
        self.desc2 = desc2

    def __str__(self):
        return f"{self.desc1}: {self.desc2}"
