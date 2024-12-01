def main():
    # Reading file
    with open("./day1.txt", "r") as file:
        lines = file.readlines()

    left_column = []
    right_column = []

    for line in lines:
        left, right = map(int, line.strip().split())
        left_column.append(left)
        right_column.append(right)

    left_column.sort()
    right_column.sort()

    # Star 1
    diffSum = 0;
    for i in range(len(left_column)):
        diffSum += abs(left_column[i] - right_column[i])
    print("Sum of differences:", diffSum);

    # Star 2
    similarity = 0;
    for i in range(len(left_column)):
        similarity += left_column[i] * countOf(left_column[i], right_column)
    print("Similarity score:", similarity)

def countOf(num, right):
    count = 0
    for i in right:
        if i == num:
            count += 1
    return count

if __name__ == "__main__":
    main()