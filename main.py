import math


def get_inputs(arg_names):
    numbers = []

    for i in range(len(arg_names)):
        number = input("Enter {}: ".format(arg_names[i]))
        try:
            number = float(number)
            print(number)
            numbers.append(number)

        except NameError:
            print("You should enter numeric input")
            return []
    return numbers


def calculate_area_perimeter_of_circle():
    [radius] = get_inputs(["radius"])
    area = math.pi * math.pow(radius, 2)
    perimeter = 2 * math.pi * radius

    print("Circle area = {} and perimeter = {}".format(area, perimeter))


def calculate_area_perimeter_of_square():
    [width] = get_inputs(["width"])
    area = width * width
    perimeter = width * 4

    print("Square area = {} and perimeter = {}".format(area, perimeter))


def calculate_area_perimeter_of_triangle():
    [rule, height] = get_inputs(["rule", "height"])
    area = rule * height / 2
    perimeter = rule * 3

    print("Triangle area = {} and perimeter = {}".format(area, perimeter))


def calculate_area_perimeter_of_trapezius():
    [rule1, rule2, rule3, rule4, height] = get_inputs(["rule 1", "rule 2", "rule 3", "rule 4", "height"])
    area = (rule1 * rule3) / 2 * height
    perimeter = rule1 + rule2 + rule3 + rule4

    print("Trapezius area = {} and perimeter = {}".format(area, perimeter))


def calculate_area_perimeter_of_polygon():
    [side, side_count, height] = get_inputs(["side", "side count", "distance of center from side "])
    perimeter = side * side_count
    area = (height * perimeter) + 2

    print("Polygon area = {} and perimeter = {}".format(area, perimeter))


def calculate_area_perimeter_of_rectangle():
    [width, height] = get_inputs(["width", "height"])
    perimeter = (width + height) * 2
    area = height * height

    print("Rectangle area = {} and perimeter = {}".format(area, perimeter))


def calculate_volume_of_sphere():
    [radius] = get_inputs(["radius"])
    volume = 4 / 3 * math.pi * math.pow(radius, 2)

    print("Sphere volume = {}".format(volume))


def calculate_volume_of_cone():
    [radius, height] = get_inputs(["radius", "height"])
    volume = 1 / 3 * math.pi * math.pow(radius, 2) * height

    print("Cone volume = {}".format(volume))


def calculate_area_perimeter_of_oval():
    [main_axis_width, sub_axis_width] = get_inputs(["width of main axis", "width of sub axis"])

    main_axis = (main_axis_width / 2)
    sub_axis = (sub_axis_width / 2)

    perimeter = 2 * math.pi * math.sqrt((math.pow(main_axis, 2) * math.pow(sub_axis, 2)) / 2)
    area = main_axis * sub_axis * math.pi

    print("Oval area = {} and perimeter = {}".format(area, perimeter))


def calc(shape_name):
    match shape_name:
        case "circle":
            return calculate_area_perimeter_of_circle
        case "square":
            return calculate_area_perimeter_of_square
        case "triangle":
            return calculate_area_perimeter_of_triangle
        case "trapezius":
            return calculate_area_perimeter_of_trapezius
        case "polygon":
            return calculate_area_perimeter_of_polygon
        case "rectangle":
            return calculate_area_perimeter_of_rectangle
        case "sphere":
            return calculate_volume_of_sphere
        case "cone":
            return calculate_volume_of_cone
        case "oval":
            return calculate_area_perimeter_of_oval
        case _:
            print("Invalid shape")


class Action:
    def __init__(self, message, run):
        self.message = message
        self.run = run


actions = [
        Action("Calculate area and perimeter of the circle", calc("circle")),
        Action("Calculate area and perimeter of the square", calc("square")),
        Action("Calculate area and perimeter of the triangle", calc("triangle")),
        Action("Calculate area and perimeter of the trapezius", calc("trapezius")),
        Action("Calculate area and perimeter of the polygon", calc("polygon")),
        Action("Calculate area and perimeter of the rectangle", calc("rectangle")),
        Action("Calculate volume of the sphere", calc("sphere")),
        Action("Calculate volume of the cone", calc("cone")),
        Action("Calculate area and perimeter of the oval", calc("oval"))
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
    action = get_action()

    print(action.message)
    action.run()
