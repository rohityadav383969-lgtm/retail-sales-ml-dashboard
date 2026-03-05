'''import matplotlib.pyplot as plt

# UNIVARIATE
def sales_distribution(df):
    fig, ax = plt.subplots()
    ax.hist(df['total_amount'], bins=30)
    ax.set_title("Sales Distribution")
    ax.set_xlabel("Total Amount")
    ax.set_ylabel("Frequency")
    return fig


# BIVARIATE
def quantity_vs_sales(df):
    fig, ax = plt.subplots()
    ax.scatter(df['quantity'], df['total_amount'])
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Total Amount")
    ax.set_title("Quantity vs Sales")
    return fig


# MULTIVARIATE
def monthly_sales_by_gender(df):
    pivot = df.pivot_table(
        values='total_amount',
        index='month',
        columns='gender',
        aggfunc='mean'
    )

    fig, ax = plt.subplots()
    pivot.plot(ax=ax)
    ax.set_title("Monthly Sales by Gender")
    return fig
'''

import matplotlib.pyplot as plt
import seaborn as sns

def sales_by_category(df):

    plt.figure(figsize=(8,5))

    sns.barplot(
        x="Product Category",
        y="Total Amount",
        data=df
    )

    plt.xticks(rotation=45)

    plt.title("Sales by Product Category")

    plt.tight_layout()

    return plt


def gender_distribution(df):

    plt.figure(figsize=(6,4))

    sns.countplot(
        x="Gender",
        data=df
    )

    plt.title("Customer Gender Distribution")

    return plt


def age_distribution(df):

    plt.figure(figsize=(6,4))

    sns.histplot(
        df["Age"],
        bins=20
    )

    plt.title("Age Distribution")

    return plt