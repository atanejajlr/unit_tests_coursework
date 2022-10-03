class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def get_area(self):
        return self.width * self.length
    
    
       
my_rect = Rectangle(10, 20)

print(my_rect.width)
print(my_rect.length)

print("Area: ", my_rect.get_area())