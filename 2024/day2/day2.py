def main():
    with open("./day2.txt", "r") as file:
        lines = file.readlines()

    reports = []

    for line in lines:
        reports.append([int(x) for x in line.strip().split()])

    partOne(reports)
    partTwo(reports)


def partTwo(reports):
    count = 0
    for report in reports:
        if checkSafety(report):
                count += 1
        else:
            print(f"original report: {report}")
            for level in range(len(report)):
                if checkSafety(report[:level] + report[level+1:]) == True:
                    print(report[:level] + report[level+1:])
                    count += 1
                    break
            
    print(f"Safe reports: {count}")



def partOne(reports):
    count = 0
    for report in reports:
        if checkSafety(report):
            count += 1
    print(f"Safe reports: {count}")

def checkSafety(report):
    if (sorted(report) != report) and (sorted(report, reverse=True) != report):
        return False

    for i in range(len(report) - 1):
        if not (0 < abs(report[i] - report[i+1]) <= 3):
            return False
        
    return True

if __name__ == "__main__":
    main()