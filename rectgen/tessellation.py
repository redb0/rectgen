import random

from .choice_func import rand_side, rand_rect


class Rectangle:
    __slots__ = ('w', 'l', 'h', 'p', 'x', 'y')

    def __init__(self, width, lenght, height=0., priority=1, x=0., y=0.):
        self.w = width
        self.l = lenght
        self.h = height
        self.p = priority
        self.x = x
        self.y = y


def split(lenght, width, x0=0, y0=0, min_size=1, side_choice=None, randgen=None):
    # функция разделения прямоугольника на два
    if min_size < 1:
        min_size = 1

    if width < 2 * min_size and lenght < 2 * min_size:
        return [Rectangle(width, lenght, x=x0, y=y0)]
    elif width < 2 * min_size and lenght >= 2 * min_size:
        l = random.randint(min_size, lenght - min_size)
        w = width
        r1 = Rectangle(w, l, x=x0, y=y0)
        r2 = Rectangle(w, lenght - l, x=x0, y=y0 + l)
    elif lenght < 2 * min_size and width >= 2 * min_size:
        w = random.randint(min_size, width - min_size)
        l = lenght
        r1 = Rectangle(w, l, x=x0, y=y0)
        r2 = Rectangle(width - w, l, x=x0 + w, y=y0)
    else:
        if side_choice is None:
            side_choice = rand_side
        if randgen is None:
            randgen = lambda x: int(random.gauss(x, x/3))
        d = side_choice(lenght, width)
        if d == 0:  # ось X
            w = randgen(lenght)  # np.random.binomial
            if not min_size <= w < width - min_size:
                w = random.randint(min_size, width - min_size)
            r1 = Rectangle(w, lenght, x=x0, y=y0)
            r2 = Rectangle(width - w, lenght, x=x0 + w, y=y0)
        else:  # ось Y
            l = randgen(width)
            if not min_size <= l < lenght - min_size:
                l = random.randint(min_size, lenght - min_size)
            r1 = Rectangle(width, l, x=x0, y=y0)
            r2 = Rectangle(width, lenght - l, x=x0, y=y0 + l)
    return [r1, r2]


def generate(n, lenght, width, height, priority_bound=None, x0=0., y0=0., **kwargs):  # tessellation
    # генерация замощения случайными прямоугольниками
    rectangles = []

    if n < 1:
        raise ValueError('The number of rectangles must be greater than 1')
    
    if not priority_bound:
        min_p, max_p = 1, 1
    else:
        min_p, max_p = priority_bound
        if min_p < 1 or max_p < 1:
            raise ValueError('Priority must be greater than 0')
        elif min_p > max_p:
            raise ValueError('Minimum priority must be less than maximum priority.')

    if n == 1:
        return Rectangle(lenght, width, height=height, min_p=min_p, max_p=max_p, x=x0, y=y0)
    else:
        rectangles = tessellation_bin(n, lenght, width, min_p=min_p, max_p=max_p, x0=x0, y0=y0, **kwargs)
        for r in rectangles:
            r.h = height
        return rectangles


def tessellation_bin(n, lenght, width, min_p=1, max_p=3, x0=0., y0=0., min_size=1, rect_choice=None, side_choice=None, prioritization=None, randgen=None):
    # создание замощения
    rectangles = []

    if prioritization is None:
        prioritization = lambda x: x + 1 if random.random() < 0.10 and x < max_p else x

    if rect_choice is None:  # предусмотреть повторный выбор если r.l == 1 and r.w == 1
        rect_choice = rand_rect

    while len(rectangles) < n:
        if len(rectangles) == 0:
            rs = split(lenght, width, x0=x0, y0=y0, min_size=min_size, side_choice=side_choice, randgen=randgen)
            if len(rs) != 2:
                continue
            r1, r2 = rs
            r1.p = min_p
            r2.p = prioritization(r1.p)
        else:
            r = rect_choice(rectangles)
            rs = split(r.l, r.w, x0=r.x, y0=r.y, min_size=min_size, side_choice=side_choice, randgen=randgen)
            if len(rs) != 2:
                continue
            rectangles.remove(r)
            r1, r2 = rs
            r1.p = prioritization(r.p)
            r2.p = prioritization(r.p)
        rectangles.append(r1)
        rectangles.append(r2)
    return rectangles


def main():
    pass

if __name__ == '__main__':
    pass
