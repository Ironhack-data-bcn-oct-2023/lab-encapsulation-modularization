import src.extraction as extract
import src.cleaning as clean
import src.visualization as viz
import pandas as pd
import os
import matplotlib

df = extract.downloading("https://raw.githubusercontent.com/Ironhack-data-bcn-oct-2023/lectures/main/datasets/avocado_kaggle.csv", "avocado_automated.csv")
df.sample()

df = clean.basic_cleaning(df, "avocado_automated_clean.csv")
df.sample()

viz.visualizing(df, "avocado_automated_fig")