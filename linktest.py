import urllib.request

f = urllib.request.urlopen("https://www.amazon.com/Graphics-PCI-Express-Auto-Extreme-Technology-DisplayPort/dp/B08Y97SRFC/ref=sr_1_2_sspa?crid=2SCEN8ZAR4W5E&dchild=1&keywords=graphic+card&qid=1615894459&sprefix=graph%2Caps%2C272&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE5M0hCT0NHTlFNU0QmZW5jcnlwdGVkSWQ9QTA5ODI3ODYxQk1VWFdaWVQyU1BTJmVuY3J5cHRlZEFkSWQ9QTA0NjMxMzMxMURDSEtPRzQ3VkpKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==").read()
print(f)