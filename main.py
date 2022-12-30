options = [
        {
            "message": "Calculate area and perimeter of the circle",
        },
        {
            "message": "Calculate area and perimeter of the square",
        },
        {
            "message": "Calculate area and perimeter of the triangle",
        },
        {
            "message": "Calculate area and perimeter of the trapezoid",
        },
        {
            "message": "Calculate area and perimeter of the polygon",
        },
        {
            "message": "Calculate area and perimeter of the rectangle",
        },
        {
            "message": "Calculate volume of the sphere",
        },
        {
            "message": "Calculate volume of the cone",
        },
        {
            "message": "Calculate area and perimeter of the oval",
        },
    ]


def get_action():
    for index in range(len(options)):
        option = options[index]
        print("options #{}: {}".format(index + 1, option.get("message")))


if __name__ == '__main__':
    get_action()
