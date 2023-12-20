import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

#6.3 You made appropriate use of a docstring in your function definition
def read_csv_data(file_path):
    """
    Reading data from a CSV file into a Pandas DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame or None: Reading the DataFrame from the CSV file or Not if the file is not found.
    """
    try:
        #8.2 You read in a CSV of data into a data frame object using pandas.
        df = pd.read_csv(file_path)
        return df

    except FileNotFoundError:
        print(f"File '{file_path}' not found. Scraping data from Goodreads instead.")
        return None
    
#6.4 You checked the help for your function to verify your docstring documentation.
#help(read_csv_data)-uncomment this to output the docstring 

#10.1 You found a simple web page and described what data you wanted to scrape from it
def scrape_data():
    """
    Scraping data from a list on the Goodreads website.

    Returns:
    - list: A list of dictionaries with information about books (title and author name).
    """
    url = "https://www.goodreads.com/list/show/19.Best_for_Book_Clubs"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []
    #10.2 You used bs4 to scrape a simple web page
    book_entries = soup.find_all('tr', itemtype="http://schema.org/Book")

    for book in book_entries:
        title = book.find('a', class_='bookTitle').get_text(strip=True)
        author = book.find('a', class_='authorName').get_text(strip=True)

        books.append({'Title': title, 'Author': author})

    return books
#help(scrape_data)-uncomment this to output the docstring 

def analyze_data(books):
    """
    Using Pandas to create a  DataFrame from the list of book and print the format. 

    Parameters:
    - books(list): A list dictionaries containing information about books.

    Returns:
    - pd.DataFrame: The DataFrame created from the list of books.
    """
    df = pd.DataFrame(books)
    print("DataFrame structure:")
    print(df.head())  #print the dataframe: this will give the first five books on the list to show the format

    return df
#help(analyze_data)-uncomment this to output the docstring 


def recommend_books(df, num_recommendations=5):
    """
    Randomly generate a subset of books from the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing info about the books.
    - num_recommendations (int): The amount of books to generate (5).

    Returns:
    - pd.DataFrame: A subset of the input DataFrame with the generated books.
    """
    #8.3 You used pandas to get a subset of a data frame using a boolean
    recommendations = df.sample(min(num_recommendations, len(df)))
    return recommendations
#help(recommend_books)-uncomment this to output the docstring 

#7.1 You used a string method to split a string into a list of smaller strings.
#only using the last name of the author for a cleaner result 
def author_names(author):
    return author.split()[-1]
"""
    Seperate the last name from a full author name.

    Parameters:
    - author (str): The full name of the author.

    Returns:
    - str: The last name of the author.
    """
#help(author_names)-uncomment this to output the docstring 

#10.3 You used ’polite’ code to scrape a web page and described your approach
csv_file_path = 'goodreads_data.csv'
existing_data = read_csv_data(csv_file_path)

if existing_data is None:
    books_data = scrape_data()
    sorted_books_df = analyze_data(books_data)

    #8.4 You wrote data that you created or changed to a CSV using pandas.
    sorted_books_df.to_csv(csv_file_path, index=False)
else:

    sorted_books_df = analyze_data(existing_data)

#8.1 You used an narray or Series to perform a vectorized computation instead of a loop or comprehension.
sorted_books_df['Author'] = sorted_books_df['Author'].apply(author_names)

#the reccomened books will be below the dataframe with its corresponding number from the list in the CSV file
print("Randomly Selected Books:")
print(recommend_books(sorted_books_df))

