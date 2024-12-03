import re

def main():
    with open("./day3.txt", "r") as file:
        lines = file.read()

    partOne(lines)
    partTwo(lines)

def partOne(lines):
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, lines)

    count = 0
    for match in matches:
        match = match[4:-1].split(",")
        count += int(match[0]) * int(match[1])

    print("Part One:", count)

def partTwo(lines):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, lines)

    count = 0
    enabled = True
    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled == True:
            match = match[4:-1].split(",")
            count += int(match[0]) * int(match[1])

    print("Part Two:", count)

if __name__ == "__main__":
    main()