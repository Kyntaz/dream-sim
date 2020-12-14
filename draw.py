from matplotlib import rcParams
rcParams['font.family'] = 'serif'

from matplotlib import pyplot as plt
import numpy as np
from mcrng import McRng
from tqdm import tqdm

dream_data = [(22,3), (5,3), (24,2), (18,2), (4,0), (1,1), (7,2), (12,5), (26,3), (8,2), (5,2), (20,2), (2,0), (13,1), (10,2), (10,2), (21,2), (20,2), (10,2), (3,1), (18,2), (3,2)]
dream_data_cum = [(0,0)]

for ings, pearls in dream_data:
    prev_ings, prev_pearls = dream_data_cum[-1]
    dream_data_cum.append((ings + prev_ings, pearls + prev_pearls))

def line_plot(file):
    with open(file) as f:
        avg = np.zeros(262)
        plt.figure(figsize=(8,5))
        c = 0
        for l in f:
            vals = eval(l)
            x = [i for i,_ in vals]
            y = [p for _,p in vals]
            plt.plot(
                x, y,
                color="tab:blue",
                alpha=0.05
            )
            norm = np.interp(np.arange(262), x, y)
            avg += norm
            c  += 1
        avg /= float(c)
        plt.plot(np.arange(262) * 20 / 423, color="tab:orange", label="Expected")
        plt.plot(avg, color="tab:red", label="Average")
        plt.plot([i for i,_ in dream_data_cum], [p for _,p in dream_data_cum], color="tab:green", label="Dream")
        plt.legend()
        plt.xlabel("Accumulated Gold Ingots", weight="bold")
        plt.ylabel("Accumulated Pearl Trades", weight="bold")
        plt.show()

def plot_compare(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        plt.figure(figsize=(8,5))
        avg1 = np.zeros(262)
        avg2 = np.zeros(262)
        c1 = 0
        c2 = 0
        for l in f1:
            vals = eval(l)
            x = [i for i,_ in vals]
            y = [p for _,p in vals]
            plt.plot(
                x, y,
                color="tab:cyan",
                alpha=0.01
            )
            norm = np.interp(np.arange(262), x, y)
            avg1 += norm
            c1 += 1
        for l in f2:
            vals = eval(l)
            x = [i for i,_ in vals]
            y = [p for _,p in vals]
            plt.plot(
                x, y,
                color="tab:pink",
                alpha=0.01
            )
            norm = np.interp(np.arange(262), x, y)
            avg2 += norm
            c2 += 1

        avg1 /= c1
        avg2 /= c2
        plt.plot(avg1, color="tab:cyan", label="Smart Player")
        plt.plot(avg2, color="tab:pink", label="Naive Player")

        plt.xlabel("Accumulated Gold Ingots", weight="bold")
        plt.ylabel("Accumulated Pearl Trades", weight="bold")
        plt.legend()
        plt.show()

def plot_dist(file, color="tab:blue"):
    with open(file) as f:
        plt.figure(figsize=(8,5))
        ps = []
        for l in f:
            vals = eval(l)
            _, p_t = vals[-1]
            ps.append(p_t)
        plt.hist(ps, color=color, histtype="bar", range=(0,max(ps)), bins=np.arange(max(ps)+1)-0.5, density=True)
        plt.axvline(np.mean(ps), color="tab:red", ls=":", label="Average")
        plt.axvline(263.0 * 20 / 423, color="tab:orange", ls=":", label="Expected")

        plt.xlabel("Accumulated Pearl Trades", weight="bold")
        plt.ylabel("Probability", weight="bold")
        plt.legend()
        plt.show()

def test_rng1(n):
    vals = []
    rng = McRng.make()
    plt.figure(figsize=(8,5))
    for _ in tqdm(range(n)):
        vals.append(rng.nextInt(423))

    plt.hist(vals, color="tab:blue", histtype="bar", range=(0,422), bins=np.arange(423)-0.5, density=True)
    plt.xlabel("Random Value", weight="bold")
    plt.ylabel("Probability", weight="bold")
    plt.show()

def test_rng2(n):
    vals = []
    plt.figure(figsize=(8,5))
    for _ in tqdm(range(n)):
        rng = McRng.make()
        vals.append(rng.nextInt(423))

    plt.hist(vals, color="tab:blue", histtype="bar", range=(0,422), bins=np.arange(423)-0.5, density=True)
    plt.xlabel("Random Value", weight="bold")
    plt.ylabel("Probability", weight="bold")
    plt.show()
