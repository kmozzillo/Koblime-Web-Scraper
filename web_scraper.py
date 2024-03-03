"""
Kevin Mozzillo - Koblime Web Scraper Project
This script takes the input from an html file called Koblime.complete
It outputs the quotes within the HTML file and outputs it to the "quotes" page within Notion

get_BookNotes() - Reads the Koblime.complete.html file and returns a list of the quotes
get_Children() - Formats the list returned in the above function and formats it JSON for Notion
main() - Retrieves the page ID and block ID of the Notion page from the Notion Key and sends a PATCH request to update the Notion page
"""

import bs4 
import requests

NOTION_KEY = ""

def get_BookNotes():
	list = []
	book_file = open('Koblime-complete.html', 'r', encoding='utf-8')
	soup = bs4.BeautifulSoup(book_file.read(), 'html.parser')
	elems = soup.select('p')
	i = 0
	while i < len(elems):
		list.append(('\"' + elems[i].getText()))
		i += 1
	book_file.close()
	return list
def get_Children():
	children = []
	for quote in get_BookNotes():
		children.append({
		"object": "block",
		"type": "paragraph",
		"paragraph": {
			"rich_text": [{ 
				"type": "text", 
				"text": { "content": quote
				}
			}]
		}
		})
	return children

def main():

	headers = {
		"Authorization": f"Bearer {NOTION_KEY}",
		"Notion-Version": "2022-06-28",
		"content-type": "application/json"
	}

	search_params = {"filter": {"value": "page", "property": "object"}}
	search_response = requests.post(
		f'https://api.notion.com/v1/search', 
		json=search_params, headers=headers)

	search_results = search_response.json()["results"]
	page_id = search_results[0]["id"]

	res = requests.get(f"https://api.notion.com/v1/blocks/{page_id}/children", headers=headers)
	block_id = res.json()["results"][7]["id"]

	create_page_body = {
		"children": get_Children()
		, "after": f"{block_id}"
	}
	
	requests.patch(f"https://api.notion.com/v1/blocks/{page_id}/children", json=create_page_body, headers=headers)

if __name__ == '__main__':
	main()
