import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

def load_data():
    df = pd.read_csv("Data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def datetime_to_days(s, reference):
    return (s - reference).dt.days

def plot_weight(df):
    plt.scatter(df["Date"], df["Weight"])
    plt.ylim([180, 320])
    plt.title("Weight Loss")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    
def plot_regression(df):
    df = df.dropna(subset = ["Weight"])
    days = datetime_to_days(df["Date"], min(df["Date"]))
    coef = np.polyfit(days, df["Weight"], 1)
    poly1d_fn = np.poly1d(coef)
    
    label = f"Average Weight Change: {coef[0]*7:.1f} lbs/week"
    
    y = [poly1d_fn(day) for day in days]
    plt.plot(df["Date"], y, "--k", label=label)
    plt.legend()
    return label


if __name__ == "__main__":
    df = load_data()
    plot_weight(df)
    print(plot_regression(df))
    plt.show()