import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    weight_data = pd.read_csv("Data.csv")
    weight_data["Date"] = pd.to_datetime(weight_data["Date"])
    important_dates = pd.read_csv("ImportantDates.csv")
    important_dates["Date"] = pd.to_datetime(important_dates["Date"])
    return weight_data, important_dates

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
    
    label = f"Average Weight Change: {coef[0]*7:.2f} lbs/week"
    
    y = [poly1d_fn(day) for day in days]
    plt.plot(df["Date"], y, "--k", label=label)
    plt.legend()
    return label
    
def plot_dates(df):
    for index, row in df.iterrows():
        plt.axvline(row["Date"], c="red")
        plt.text(row["Date"], 280, row["Label"], c="red", rotation="vertical", horizontalalignment='center',
            verticalalignment='center', bbox={"facecolor":"white", "edgecolor":"white"})


if __name__ == "__main__":
    weight_data, important_dates = load_data()
    plot_weight(weight_data)
    print(plot_regression(weight_data))
    plot_dates(important_dates)
    plt.show()