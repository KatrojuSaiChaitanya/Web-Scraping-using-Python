# Email-Phone scraping

This project allows you to easily crawl through the websites' script to 
collect bulk of emails and phone numbers which are then dumped into a .csv file
in an organized way.

The main concern of this 'Advanced' Email and phone scraping using python3 is to
provide a platform where we can garner the data (emails and phone no:) in a neat and 
swift manner.

## Applications:

1. Generally used by marketers to stockpile the data of several organizations.
2. Used in Business/ eCommerce: Market Analysis


# Getting Started

These instructions will help you to deploy this project in your local systems for development and testing purposes.
Given below are the steps to be followed systematically to build this project.

# Pre-requisites

What are the things which are to be installed in your system?

- This project is built using python version 3.7 

Libraries to be installed ?          
                                              
1.  pip install regex                         (2020.7.14)
2.  pip install google-search                 (1.0.2)
3.  pip install requests                      (2.24.0)
5.  pip install beautifulsoup4                (4.9.1)
6   pip install tld                           (0.12.2)

# Deployment

Now you are good to go :)

1. Clone and download the zip file.
2. Extract the file into your required directory.
3. Erase the content in the .csv file and keep the header undisturbed.
4. Run the script 

# Execution

1. Enter the organization name along with the location if necessary. 
   Ex: Deloitte Hyderabad
2. The link associated with it will be stored in the 'web_urls.txt'
3. Enjoy Harvesting Emails and Phone numbers :)

# How does it Work?

1. Firstly, It generates a link for the input which is being provided. This, It does using 'search' from the google-search librarya and stores successively in the 'web_urls.txt' 
2. Secondly, We now process each and every URL by requesting a HTTP response to the website.
3. We convert the entire page of that respective url into a html scripted text using bs4.
4. Now that we have extracted the entire content from the web page, we have to scrap all the emails and phone numbers present in the home page.
5. The scraping of the data is all done by regular expressions.
6. The regex code employed in this project is the one which is generalized, which detects and throws back mails along with phone no's from most of the websites. Nevertheless,      for some it might not detect.
7. If the data is not detected in the home page of the website, It traces the contact page and starts collecting the data if present, as most of the websites' contact              details reside in the contact-us webpage
8. Now we merge the home page data and contact page data into a single data structure.
9. Finally, We dump the entire stuff into a csv file, so that the data is not in a dishevelled manner.

# Built with

Python 3.x

# Contributing

Open to contributions from the public.


# Author

- K Sai Chaitanya 

