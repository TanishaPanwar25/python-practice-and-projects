# import requests
# from bs4 import BeautifulSoup


# url = "https://www.flipkart.com/search?q=iphone+13"

# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Accept-Language": "en-US,en;q=0.9"
# }

# response = requests.get(url, headers=headers)
# print(response.text[:1000])      # <-- Add this line
# soup = BeautifulSoup(response.text, "lxml")
# soup = BeautifulSoup(response.text, "lxml")

# products = soup.find_all("div", class_="_13oc-S")

# for p in products:
#     # Name
#     name = p.find("div", class_="_4rR01T")
#     name = name.get_text() if name else "N/A"

#     # Price
#     price = p.find("div", class_="_30jeq3")
#     price = price.get_text() if price else "N/A"

#     # Rating
#     rating = p.find("div", class_="_3LWZlK")
#     rating = rating.get_text() if rating else "No Rating"

#     # Image
#     image = p.find("img", class_="_396cs4 _3exPp9")
#     image = image["src"] if image else "No image"

#     print(name, price, rating, image)

# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"

# # Step 1: Fetch HTML
# response = requests.get(url)

# # Step 2: Parse HTML
# soup = BeautifulSoup(response.text, "lxml")

# # Step 3: Identify product blocks
# books = soup.find_all("article", class_="product_pod")

# # Step 4: Extract data
# for b in books:
#     title = b.h3.a["title"]
#     price = b.find("p", class_="price_color").get_text()
#     image = "https://books.toscrape.com/" + b.find("img")["src"]

#     print("Title:", title)
#     print("Price:", price)
#     print("Image:", image)
#     print("-" * 40)


import requests
import json
import pandas as pd

url = "https://www.rekhta.org/tags/famous-shayari/couplets?lang=hi"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

# STEP 1: Request
response = requests.get(url, headers=headers)
data = response.json()

# STEP 2: See JSON structure
print(json.dumps(data, indent=4))

# STEP 3: Extract products
products = data["products"]

final_list = []

for p in products:
    final_list.append({
        "title": p.get("title"),
        "price": p.get("price"),
        "rating": p.get("rating"),
        "brand": p.get("brand"),
        "thumbnail": p.get("thumbnail"),
        "first_image": p.get("images", [None])[0]
    })

# STEP 4: Convert to DataFrame
df = pd.DataFrame(final_list)

# STEP 5: Save
df.to_csv("products.csv", index=False)

print(df.head())

