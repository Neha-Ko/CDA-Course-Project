"""Shared helper functions for the Sephora moisturizer review project."""
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../Data/sephora_moisturizer_reviews_clean.csv.gz"


def load_data(path=DATA_PATH):
    """Load the cleaned review dataset with dates parsed."""
    return pd.read_csv(path, parse_dates=["submission_time"])


def share_table(df, col):
    """Counts and percentages for one column."""
    counts = df[col].value_counts()
    return pd.DataFrame({"count": counts, "pct": (counts / counts.sum() * 100).round(1)})


def plot_bar(series, title, xlabel, ylabel, rot=0):
    """Simple single-color bar chart. Use rot to angle the x-axis labels."""
    ax = series.plot(kind="bar", color="#4C72B0", figsize=(7, 4), rot=rot)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if rot:
        plt.setp(ax.get_xticklabels(), ha="right")
    ax.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    plt.show()