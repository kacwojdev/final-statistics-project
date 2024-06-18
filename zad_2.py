import numpy as np
import pandas as pd

def calculate_statistics(vector):
    if not isinstance(vector, (list, np.ndarray)):
        raise ValueError("Wejście musi być listą lub numpy array")
    if len(vector) == 0:
        raise ValueError("Wektor nie może być pusty")
    
    vector = np.array(vector)
    
    mean = np.mean(vector)
    std_dev = np.std(vector, ddof=1)
    minimum = np.min(vector)
    percent_10 = np.percentile(vector, 10)
    quartile_1 = np.percentile(vector, 25)
    median = np.median(vector)
    quartile_3 = np.percentile(vector, 75)
    percent_90 = np.percentile(vector, 90)
    maximum = np.max(vector)
    range_ = maximum - minimum
    iqr = quartile_3 - quartile_1
    
    n = len(vector)
    skewness = (n * np.sum((vector - mean)**3)) / ((n - 1) * (n - 2) * std_dev**3)
    
    kurtosis = (n * (n + 1) * np.sum((vector - mean)**4)) / ((n - 1) * (n - 2) * (n - 3) * std_dev**4) - (3 * (n - 1)**2) / ((n - 2) * (n - 3))
    
    statistics = {
        "średnia": mean,
        "odchylenie standardowe": std_dev,
        "współczynnik zmienności": std_dev / mean if mean != 0 else np.nan,
        "minimum": minimum,
        "10 percentyl": percent_10,
        "1 kwartyl": quartile_1,
        "mediana": median,
        "3 kwartyl": quartile_3,
        "90 percentyl": percent_90,
        "maksimum": maximum,
        "rozstąp danych": range_,
        "rozstęp międzykwartylowy": iqr,
        "skośność": skewness,
        "kurtoza": kurtosis
    }
    
    df = pd.DataFrame(statistics.items(), columns=["Nazwa statystyki", "Wartość"])
    
    return df

def run():
    sample_vector = [3.5, 2.1, 5.6, 7.8, 1.2, 4.4, 8.9, 3.3, 6.7, 9.0, 3.1]
    statistics_df = calculate_statistics(sample_vector)
    
    print(statistics_df)

if __name__ == "__main__":
    run()
