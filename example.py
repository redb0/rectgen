from rectgen import generate, visualize, distribution
from rectgen.choice_func import get_setp_func


def main():
    lenght, width, height = 50, 25, 3
    n = 20

    rectangles = generate(n, lenght, width, height, min_size=3, prioritization=get_setp_func(0.2, 4))

    visualize(lenght, width, rectangles)
    distribution(lenght, width, rectangles)


if __name__ == '__main__':
    main()
