###############################
#....define the Rectangle class here
###############################
class Rectangle:
    # Constructor, gets width and heigh
    def __init__(self, h, w): 
        self.h, self.w = int(h), int(w)

    # Gets rectangle perimeter
    def getPerimeter(self):
        return 2 * (self.h + self.w)

    # Gets rectangle area
    def getArea(self):
        return self.h * self.w

    # Creates rectangle display string
    def showRectangle(self):
        return "\n" + f"{'* ' * self.w}\n" * self.h

# Main function
def main():
    # Program title
    print("Rectangle Calculator\n")

    # Get and display rectangle info until quit
    cont_flag = True
    while cont_flag:
        try:
            # Gets rectangle width and height
            h = int(input("Height:    "))
            w = int(input("Width:     "))

            # Checks to make sure a rectangle and not a line
            if h < 2 or w < 2:
                raise Exception("Both height and width must be 2 or larger! Try again...")
            
            # Creates and prints rectangle and info
            rect = Rectangle(h, w)
            print(
                f"Perimeter: {rect.getPerimeter()}\n"
                f"Area:      {rect.getArea()}\n"
                f"{rect.showRectangle()}"
            )

            # Ask if user wants to continue
            cont = input("Continue? (y/n): ").lower()
            print()

            # If user wants to quit, end loop
            if cont != "y":
                cont_flag = False

        # Exception for bad inputs
        except Exception as e:
            print(f'{e}\n')

    # See you later :)
    print("Bye!")

# If running file directly, not imported
if __name__ == "__main__":
    main()
