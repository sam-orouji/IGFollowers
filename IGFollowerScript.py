from bs4 import BeautifulSoup 
#download instagram zip file first - took me about .5 -1h to get the files from IG - search on internet how to download
#make sure to delete folder/zip files when done bc it contains sensitive data: DMs, personal info like contacts, address, IP, etc.

#extract accounts of followers/following from html file in your zip file


# Load the HTML content - replace with your followers HTML body content
followers_html_content = """ """

# Parse the HTML
followers_parsed = BeautifulSoup(followers_html_content, 'lxml')

# Find all <a> tags with href containing "instagram.com"
links1 = followers_parsed.find_all('a', href=lambda x: x and 'instagram.com' in x)

# Extract handles and store in a list
followers = [link.get_text(strip=True) for link in links1]

# Print the followers (for verification)
print(followers)

print("\n\n\n")




# Load the HTML content - replace with your following HTML body content
following_html_content = """ """
# Parse the HTML
following_parsed = BeautifulSoup(following_html_content, 'lxml')

# Find all <a> tags with href containing "instagram.com"
links2 = following_parsed.find_all('a', href=lambda x: x and 'instagram.com' in x)

# Extract handles and store in a list
following = [link.get_text(strip=True) for link in links2]

# Print the following (for verification)
print(following)





# now compare the two lists & print people not following back
not_following_back = []
count = 1
for person in following:
    if person not in followers:
        print(person)
        count+=1
print(count)
