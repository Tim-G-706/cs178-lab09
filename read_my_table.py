# read_my_table.py
# Reads all items from the DynamoDB Books table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Attr, Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Books"


def get_table():
    """Return a reference to the DynamoDB Book table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_books(books):
    title = books.get("Title", "Unknown Title")
    pages = books.get("Pages", "Unknown Number of Pages")

    print(f"  Title  : {title}")
    print(f"  Pages   : {pages}")
    print()



def print_all_books():
    """Scan the entire Movies table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No Books found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} book(s):\n")
    for book in items:
        print_books(book)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_books()


if __name__ == "__main__":
    main()