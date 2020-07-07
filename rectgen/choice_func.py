import sys
import random
from inspect import getmembers, isfunction


def get_functions(suffix):
    return [obj for obj, name in getmembers(sys.modules[__name__]) 
            if isfunction(obj) and name.endswith(suffix)]


# Функции выбора прямоугольника
def rand_rect(rectangles, p=None):
    r = rectangles[random.choice(range(len(rectangles)))]
    while r.l == 1 and r.w == 1:
        r = rectangles[random.choices(range(len(rectangles)), weights=p, k=1)[0]]
    return r


def prob_by_lenght_rect(rectangles):
    p = [r.l / sum(el.l for el in rectangles) for r in rectangles]
    return rand_rect(rectangles, p=p)


def prob_by_width_rect(rectangles):
    p = [r.w / sum(el.w for el in rectangles) for r in rectangles]
    return rand_rect(rectangles, p=p)


def prob_by_area_rect(rectangles):
    total_area = sum(r.w * r.l for r in rectangles)
    p = [(r.w * r.l) / total_area for r in rectangles]
    return rand_rect(rectangles, p=p)


def prob_by_ratio_rect(rectangles):
    p = [max(r.l, r.w) / min(r.l, r.w) for r in rectangles]
    p = [_p / sum(p) for _p in p]
    return rand_rect(rectangles, p=p)


def prob_by_ratio_area_rect(rectangles):
    total_area = sum(r.w * r.l for r in rectangles)
    p = [max(r.l, r.w) * (r.w * r.l) / min(r.l, r.w) * total_area for r in rectangles]
    return rand_rect(rectangles, p=p)


RECT_CHOICE_FUNC = get_functions('_rect')


# Функции выбора стороны
def rand_side(lenght, width):
    return random.choice([0, 1])


def probabilistic_side(lenght, width):
    p = [width / (lenght + width), lenght / (lenght + width)]
    return random.choice([0, 1], p=p)


def long_side(lenght, width):
    if lenght > width and lenght / width > 3.0:
        return 1
    elif width > lenght and width / lenght < 3.0:
        return 0
    else:
        return random.choice([0, 1])


SIDE_CHOICE_FUNC = get_functions('_side')


def random_method_side_choice(*args, p=None):
    return SIDE_CHOICE_FUNC[random.choice(range(len(SIDE_CHOICE_FUNC)), p=p)]


def random_method_rect_choice(*args, p=None):
    return RECT_CHOICE_FUNC[random.choice(range(len(RECT_CHOICE_FUNC)), p=p)]


def get_setp_func(probability, max_priority):
    def prioritization(p):
        if random.random() < probability and p < max_priority:
            return p + 1
        else:
            return p
    return prioritization
