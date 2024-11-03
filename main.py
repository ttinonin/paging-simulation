import sys

def print_mem(pages, page_index, is_hit):
    for index, i in enumerate(pages):
        if index == page_index:
            if is_hit:
                print(f"[{i}] <- (hit)")
            else:
                print(f"[{i}] <- (miss)")
        else:
            print(f"[{i}]")

def fifo(sequence, pages, n_pages):
    hit_rate = 0
    miss_rate = 0
    queue = []
    page_index = 0
    is_full = False
    hit_location = -1

    for sequence_index, i in enumerate(sequence):
        is_hit = False

        for page_pos, j in enumerate(pages):
            if sequence_index == n_pages:
                is_full = True

            if i == j:
                hit_rate += 1
                hit_location = page_pos
                is_hit = True
                break

        if not is_hit:
            queue.append(page_index)
            miss_rate += 1

        if not is_hit:
            if is_full:
                page_index = queue.pop(0)
                pages[page_index] = i
            else:
                pages[page_index] = i
        else:
            page_index = hit_location

        print(f"page: {i}")
        print_mem(pages, page_index, is_hit)
        print()

        if not is_hit:
            if page_index == n_pages - 1:
                page_index = 0
            else:
                page_index += 1

    print(f"Hit rate: ({hit_rate}/{len(sequence)})")
    print(f"Miss rate: ({miss_rate}/{len(sequence)})")

def lru_remove_lowest(recent):
    lowest = float('inf')
    lowest_key = -1
    lowest_page_index = -1

    for i in recent:
        if recent[i]["sequence_index"] < lowest:
            lowest = recent[i]["sequence_index"]
            lowest_key = i
            lowest_page_index = recent[i]["page_index"]

    recent.pop(lowest_key)

    return lowest_page_index

def lru(sequence, pages, n_pages):
    recent = {}

    hit_rate = 0
    miss_rate = 0
    is_full = False
    page_index = 0
    hit_location = -1

    for sequence_index, number in enumerate(sequence):
        is_hit = False

        for page_pos, page in enumerate(pages):
            if sequence_index == n_pages:
                is_full = True

            if number == page:
                hit_rate += 1
                is_hit = True
                page_index = page_pos
                break
        
        if is_full and not is_hit:
            page_index = lru_remove_lowest(recent)

        recent[number] = {
            "sequence_index": sequence_index,
            "page_index": page_index
        }

        pages[page_index] = number

        print(f"page: {number}")
        print_mem(pages, page_index, is_hit)
        print()

        if not is_full:
            if page_index == n_pages - 1:
                page_index = 0
            else:
                page_index += 1

        if not is_hit:
            miss_rate += 1

    print(f"Hit rate: ({hit_rate}/{len(sequence)})")
    print(f"Miss rate: ({miss_rate}/{len(sequence)})")

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