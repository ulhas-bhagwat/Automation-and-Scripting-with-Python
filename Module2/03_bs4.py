from bs4 import BeautifulSoup

html_content = """
<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Use soup.find() to locate the <h1> tag and store the extracted text in a variable called 'product_name'.
### YOUR CODE HERE ###
heading_tag = soup.find('h1')
product_name = heading_tag.get_text()
print(f"Product name: {product_name}")

# Use soup.find() to locate <p> tags with class_='price' and store the extracted text in a variable called 'price'.
### YOUR CODE HERE ###

price = soup.find('p', class_='price').get_text()
print(f"Price: {price}")

# Use soup.find() to locate <p> tags with class_='description' and store the extracted text in a variable called 'description'.
### YOUR CODE HERE ###
description = soup.find('p', class_='description').get_text()
print(f"Description: {description}")

# Print the extracted data in the format:

#print(f"Price: {price}")
#print(f"Description: {description}") 