import requests
image_url = input("Enter URL: ")
image = requests.get(image_url)
image_name = input("Enter name of image: ")
image_type = input("Enter image file type: ")
with open(f'{image_name}.{image_type}',"wb") as file:
    file.write(image.content)