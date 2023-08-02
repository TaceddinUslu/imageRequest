import tkinter
import requests
from bs4 import BeautifulSoup
import os

window =tkinter.Tk()
window.title("RequestsImageAPI")
window.minsize(300,150)

def download_images():
    print("Downloading images...")
    url = Enter_url_entry.get()
    print(f"URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    if not os.path.exists('images'):
        os.makedirs('images')

    images = soup.find_all('img')
    print(f"Found {len(images)} images")

    for image in images:
        image_url = image.get('src')
        if image_url and not image_url.startswith('data:'):
            print(f"Downloading image from {image_url}")
            image_name = os.path.basename(image_url)
            response = requests.get(image_url)
            with open(f'images/{image_name}', 'wb') as f:
                f.write(response.content)

    print("Done!")

    Enter_url_entry.delete(0, tkinter.END)




### tkinter
space = tkinter.Label(height=1)
space.pack()

Enter_url_label = tkinter.Label(text="Enter URL")
Enter_url_label.pack()


Enter_url_entry = tkinter.Entry(width=35)
Enter_url_entry.pack(pady=10)


download_button = tkinter.Button(text="Download Images", command=download_images)
download_button.pack()
### request





















window.mainloop()