from threaderf11 import main
from notion import make_box_page

ip = str(input("whats the ip?\n:"))
box_name = input("whats the Box called?")

nmap_output = main(ip)

page_data = make_box_page(box_name, nmap_output)

# If i want page data uncomment
#print(page_data)
# full,thread = scans(ip)

# print(thread)

# page id for TODO


