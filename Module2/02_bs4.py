from bs4 import BeautifulSoup

# Sample HTML content (replace with your actual HTML)
html_content = """
<html>
<body>
    <div id="main-content">
        <h1>This is a heading</h1>
        <p class="important">This is an important paragraph.</p>
        <a href="https://www.example.com">Visit Example</a>
    </div>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Use CSS selector to find the 'div' with id 'main-content'
main_content = soup.select_one('#main-content')

print(main_content.prettify())  # Output the formatted HTML of main-content
print("=============================")

# Find the 'p' element with class 'important' within 'main-content'
important_paragraph = main_content.select_one('.important')

# Extract the text content of the paragraph
paragraph_text = important_paragraph.get_text()
print(paragraph_text)  # Output: This is an important paragraph.

# Find the 'a' element within 'main-content'
link1 = main_content.find('a')
print(link1.text)  # Output: Visit Example

link = main_content.find('a')
print(link)  # Output: <a href="https://www.example.com">Visit Example</a>
print(type(link))  # Output: <class 'bs4.element.Tag'>

# Access the 'href' attribute of the link
link_url = link['href']
print(link_url)  # Output: https://www.example.com