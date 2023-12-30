import browsercookie

# Get cookies from the default browser (e.g., Chrome, Firefox)
cookies = browsercookie.chrome()

# Print the cookies
for cookie in cookies:
    print(cookie.name, cookie.value)

