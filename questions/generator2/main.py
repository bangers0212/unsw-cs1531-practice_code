from neighbours import neighbours


def main():
    iterable = [1, 2, 3, 4, 5, 6]
    for tuple in neighbours(iterable):
        print("Tuple is:", tuple)


if __name__ == "__main__":
    main()
