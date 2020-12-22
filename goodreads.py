import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bar_plot_ratings(rating_count_dict):
    # Bar chart for ratings
    ratings = list(rating_count_dict.keys())
    count_results = list(rating_count_dict.values())
    plt.bar(ratings,count_results, color='red')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
    plt.xlabel('My Rating')
    plt.ylabel('Count')
    for i in range(len(ratings)):
        plt.annotate(str(count_results[i]), xy=(ratings[i],count_results[i]), ha='center', va='bottom')
    plt.show()

def scatter_plot_ratings(avg_rating, my_rating):
    colors = np.array(["r", "b", "g"])
    area = np.pi*3
    fig, ax = plt.subplots()
    ax.scatter(avg_rating, my_rating, s=np.pi*3, c=colors[0], alpha=1)
    plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='x', alpha=0.1)
    plt.title('My Rating vs Average Rating')
    plt.xlabel('Average Rating')
    plt.ylabel('My Rating')
    plt.show()


books_df = pd.read_csv("goodreads_library_export.csv")
read_books = books_df[books_df['Date Read'].notnull()]
read_books_filter = read_books[['Title','Author','ISBN','My Rating','Average Rating','Publisher']]
rating_count = read_books_filter['My Rating'].value_counts()
bar_plot_ratings(rating_count.to_dict())
title = read_books_filter['Title']
scatter_plot_ratings(read_books_filter['Average Rating'], read_books_filter['My Rating'])