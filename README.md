# Koblime-Web-Scraper
Work in Progress: Python script that parses an HTML file, retrieves the highlights, and outputs it to a Notion block

This is a project I took on mainly for my own personal use and for learning experience. While reading with my Kobo Libra 2, I often highlight text that I find informative, creative, funny, or important. 
I use [Koblime](https://kobli.me/) as an integration which stores all my highlights and notes for books I sideload. I like to copy down my highlights to a [Notion](https://www.notion.so/) page along with writing a summary and review of the book's main theme and plot.

The goal of this project is to provide a simple method of transferring my notes from Koblime to my Notion page. 

Learning goals/topics include:
- Parsing data with the [beautiful soup](https://beautiful-soup-4.readthedocs.io/en/latest/) module
- Working with an [API](https://developers.notion.com/).
- Parsing JSON

While this script currently satisfies my needs, I am still working on ways to improve the script.

## Ideas
- Query and parse the highlights directly from the Kobo Libra 2 eReader. I'll have to look into where the highlights are locally stored
- Figure out a better way to run the Python script
