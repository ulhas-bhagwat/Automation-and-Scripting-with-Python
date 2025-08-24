from bs4 import BeautifulSoup

# Sample HTML content (replace with your actual HTML)
html_content = """
<html>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <p class="special">This is another paragraph.</p>
</body>
</html>
"""

# parse html content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the first 'p' element
first_paragraph = soup.find('p')
print("First paragraph:", first_paragraph.text)

# find all 'p' elements
all_paragraphs = soup.find_all('p')
print("All paragraphs:")
for p in all_paragraphs:
    print(p.text)

# Find the 'p' element with the class 'special'
special_paragraph = soup.find('p', class_='special')
if special_paragraph:
    print("Special paragraph:", special_paragraph.text)
