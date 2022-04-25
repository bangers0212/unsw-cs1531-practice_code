from bad_interview import bad_interview

# Just for testing, changes have already been made


def main():
    n = int(input())
    for i in bad_interview(n):
        print("Functions yields:", i)


if __name__ == "__main__":
    main()
