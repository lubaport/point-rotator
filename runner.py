from rotator import Rotator


def read_file(file):
    buffer_lines = file.readlines()
    lines = [line.decode("utf-8").strip() for line in buffer_lines]
    rotation_angle = float(lines[0])
    words = lines[1].split(",")
    y_ref = float(words[1])
    x_ref = float(words[2])
    points = {}
    for i in range(2,len(lines)):
        words = lines[i].split(",")
        points[words[0]] = {"y": float(words[1]), "x": float(words[2]), "z": float(words[3])}
    return rotation_angle, y_ref, x_ref, points


# Press the green button in the gutter to run the script.
def run_rotator(file):
    output = []
    rotation_angle, y_ref, x_ref, points = read_file(file)
    rotator = Rotator(rotation_angle, x_ref, y_ref)
    for name, key in points.items():
        x, y, z = rotator.rotate_point(key["x"], key["y"], key["z"])
        line = f"{name},{y},{x},{z}"
        output.append(line)

    return "\n".join(output)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
