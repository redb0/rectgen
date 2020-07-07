from random import random

import matplotlib.pyplot as plt
from matplotlib import patches


def patch_rect(axis, xy, lenght, width, **kwargs):
    obj = axis.add_patch(
        patches.Rectangle(xy, width, lenght, **kwargs)
    )
    return obj


def visualize(lenght, width, rectangles):
    fig, axis = plt.subplots(1, 1)
    patch_rect(axis, (0, 0), lenght, width, hatch='x', fill=False)
    for i, r in enumerate(rectangles):
        obj = patch_rect(axis, (r.x, r.y), r.l, r.w, color=(random(), random(), random()), ec='k', lw=0.5)
        axis.text(r.x + 0.5 * r.w, r.y + 0.5 * r.l, str(i), fontsize=10, ha='center', va='center')
    axis.set_xlim(0, width)
    axis.set_ylim(0, lenght)
    axis.set_xlabel('$x$')
    axis.set_ylabel('$y$', rotation=0)
    axis.set_aspect('equal', adjustable='box')
    plt.show()


def distribution(lenght, width, rectangles):
    fig, axes = plt.subplots(1, 4, figsize=(12, 5))
    axes[0].hist([r.l / lenght for r in rectangles])
    axes[0].title.set_text('Relative length')
    axes[0].grid()
    axes[1].hist([r.w / width for r in rectangles])
    axes[1].title.set_text('Relative width')
    axes[1].grid()
    axes[2].hist([max(r.l, r.w) / min(r.l, r.w) for r in rectangles], density=True)
    axes[2].title.set_text('Ratio of maximum to minimum side')
    axes[2].grid()
    axes[3].hist([r.p for r in rectangles])
    axes[3].title.set_text('Priorities')
    axes[3].grid()
    plt.subplots_adjust(left=0.05, right=0.95, wspace=0.3)
    plt.show()