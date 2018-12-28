# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import math

matplotlib.rcParams['text.usetex'] = True


def draw_exp1():
    # gencliq
    d1 = to_log((570, 57, 4, 4203, 99))
    # cliq
    d2 = to_log((220, 107, 60, 1013, 1206))

    xticks = ('$q_1$', '$q_2$', '$q_3$', '$q_4$', '$q_5$')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5 + 0.08

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time $LogT$ (s)', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=10)

    # plt.tight_layout()
    plt.savefig('exp1.pdf', format='pdf')

    plt.show()


def draw_exp2():
    # two pictures in one row, now draw the first picture
    plt.subplot(121)
    # gencliq
    d1 = (57, 123, 759)
    # cliq
    d2 = (107, 287, 854)

    xticks = ('LJ', 'OK', 'UK')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.xlabel('(a) Query $q_2$', fontsize=25)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    plt.tight_layout(pad=3)

    # two pictures in one row, now draw the second picture
    plt.subplot(122)
    # gencliq
    d1 = (57, 123, 759)
    # cliq
    d2 = (107, 287, 854)

    xticks = ('LJ', 'OK', 'UK')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.xlabel('(b) Query $q_5$', fontsize=25)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp2.pdf', format='pdf')
    plt.show()


def draw_exp2_q2():
    # gencliq
    d1 = (57, 123, 759)
    # cliq
    d2 = (107, 287, 854)

    xticks = ('LJ', 'OK', 'UK')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp2-1.pdf', format='pdf')

    plt.show()


def draw_exp2_q5():
    # gencliq
    d1 = (99, 43.6, 1253)
    # cliq
    d2 = (1206, 136, 5908)

    xticks = ('LJ', 'OK', 'UK')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp2-2.pdf', format='pdf')

    plt.show()


def draw_exp3():
    # gencliq
    d1 = (91, 68, 57)

    # cliq
    d2 = (156, 131, 106)

    xticks = ('6', '8', '10')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='GenCliqJoin', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='CliqueJoin', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.xlabel('Number of Machines', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp3.pdf', format='pdf')

    plt.show()


def to_log(arr):
    arr = np.array(arr)
    new_arr = []
    for a in arr:
        new_arr.append(math.log(a, 2))
    return tuple(new_arr)


def draw_exp4():
    # DG01
    d1 = to_log((14, 1, 1, 2, 2, 3))
    # DG03
    d2 = to_log((55, 1, 2, 4, 4, 6))
    # DG10
    d3 = to_log((170, 4, 7, 16, 15, 17))
    # DG30
    d4 = to_log((1973, 11, 22, 55, 61, 48))
    # DG60
    d5 = to_log((6282, 22, 44, 114, 207, 95))
    xticks = ('$q_1$', '$q_2$', '$q_3$', '$q_4$', '$q_5$', '$q_6$')

    dim = len(d1)

    w = 1.5
    dimw = w / dim / 1.5

    # 对列进行画图
    color = ('w', 'gray', 'b', 'g', 'c', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='DG01', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='DG03', edgecolor='k', hatch='xxx')
    plt.bar(index + 2 * dimw, d3, width=dimw, color=color[0], label='DG10', edgecolor='k', hatch='+++')
    plt.bar(index + 3 * dimw, d4, width=dimw, color=color[0], label='DG30', edgecolor='k', hatch='***')
    plt.bar(index + 4 * dimw, d5, width=dimw, color=color[0], label='DG60', edgecolor='k', hatch='OOO')

    plt.xticks(index + 2 * dimw, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time $logT$ (s)', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + 2 * dimw, d3):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + 3 * dimw, d4):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + 4 * dimw, d5):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp4.pdf', format='pdf')

    plt.show()


def draw_exp5():
    # q1 in 6, 8, 10 machines
    d1 = (247, 192, 170)

    # q4 in 6, 8, 10 machines
    d2 = (25, 19, 16)

    xticks = ('6', '8', '10')

    dim = len(d1)
    w = 1.5
    dimw = w / dim / 1.5

    # 对两个列进行画图
    color = ('w', 'gray', 'k')
    index = np.arange(dim)
    plt.bar(index, d1, width=dimw, color=color[0], label='$q_1$', edgecolor='k', hatch='///')
    plt.bar(index + dimw, d2, width=dimw, color=color[0], label='$q_4$', edgecolor='k', hatch='xxx')
    plt.xticks(index + dimw / 2, xticks)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel('Query Time (s)', fontsize=15)
    plt.xlabel('Number of Machines', fontsize=15)
    plt.legend(fontsize=12)

    for a, b in zip(index, d1):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    for a, b in zip(index + dimw, d2):
        plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    # plt.tight_layout()
    plt.savefig('exp5.pdf', format='pdf')

    plt.show()


# draw_exp1()
# draw_exp2()
# draw_exp2_q2()
# draw_exp2_q5()
# draw_exp3()
draw_exp4()
# to_log((1, 2, 3, 4))
# draw_exp5()
