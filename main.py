def calc():
    print("hello")


class Action:
    def __init__(self, message, run):
        self.message = message
        self.run = run


actions = [
        Action("Calculate area and perimeter of the circle", calc),
        Action("Calculate area and perimeter of the square", calc),
        Action("Calculate area and perimeter of the triangle", calc),
        Action("Calculate area and perimeter of the trapezoid", calc),
        Action("Calculate area and perimeter of the polygon", calc),
        Action("Calculate area and perimeter of the rectangle", calc),
        Action("Calculate volume of the sphere", calc),
        Action("Calculate volume of the cone", calc),
        Action("Calculate area and perimeter of the oval", calc)
    ]

def get_action():
    for index in range(len(actions)):
        action = actions[index]
        print("options #{}: {}".format(index + 1, action.message))

    selected_actions = input("Enter number of desired action: ")

    try:
        selected_actions_index = int(selected_actions) - 1
        return actions[selected_actions_index]

    except NameError:
        print("Invalid action selected, pleas try again")
        get_action()


if __name__ == '__main__':
    print(get_action().message)
