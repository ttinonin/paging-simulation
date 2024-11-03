import sys

def main():
    if len(sys.argv) != 3:
        print("Error: Incorrect number of argument values.")
        print("Usage: python main.py <number_of_pages> <sequence_of_pages_separeted_by_coma>")
        sys.exit()

    n_pages = int(sys.argv[1])
    sequence = (sys.argv[2]).split(",")
    sequence = [int(x) for x in sequence]
    pages = [-1 for x in range(n_pages)]

if __name__ == "__main__":
    main()