What does my program do:

The purpose of my code is to find book recommendation for my bookclub!
I'm going to use a premade list of the "best books for bookclubs" on the website goodreads.com
Starting off I'm going to input requests - for HTTP, BeautifulSoup - for Webscraping, Pandas - for data anlysis, and random - for a recommendations chosen at random.
For the next segment I created the "read_csv_data" function to read data from the CSV file and put that into a pandas Dataframe.
I then created a function called "scrape_data" to scrape the data from Goodreads website. 
I used the "requests" to get the HTML content from Goodreads. 
I then used "BeautifulSoup" to analyze and search for certain things in the HTML like author and tittle. 
I used "itemtype" with the value schema.org/books to use their vocabulary for attributes that decribe books(for HTML). 
"analyze_data" was function I made to create a Dataframe from the list of "best books for bookclubs" on goodreads and it's structure. 
My "recommend_books" function is just to randomly generated books from the Dataframe(becasue in the function above I created the Dataframe from the Goodreads list).
For the purpose of having a cleaner look when the results are printed, I created the function "author_names" to only use the authors last name. 
In the next part, the code checks the CSV file with the Goodreads data exists.
If it exist, we use that data and if not, the code will scrape the data from Goodreads,analyze and save it to a CSV file. 
Going back to the "author_names" function, I used it to modify the Dataframe and just use the authors last name when printing the recommendations. 
Laslty, the code prints the randomly selected books from the Dataframe using my "recommend_books" function. 
We succefuly have five book recommendations with the authors last printed for my bookclub to chose from!

Addiontonal Comments:
In each function I made, I used a docstring in for my function deifntion. 
After the function I commented "help(function)" for each one in order to verify the docstring documentation (uncomment in order to use).

How to use my program:

1. Running the Program:
   You must have python installed to run the program.
2. Program Execution:
    The program will check if a CSV file with the Goodreads data exists.
    If it exist, it will use that data. 
    If not, the program will scrape the data from Goodreads, analyze and save it to a CSV file.
3. Viewing the Results:
    First the structure of the Dataframe will be printed, showing the first five books on the list along with the authors first and last name.
    The program will then modify and only the authors last name will be printed for the next part.
    Lastly, five randomly generated books will be printed from the List.  
4. Optional: 
    At any point the user can uncomment any of the "help(function)" in order to print the docstring defintion of the functions in the program. 
    