import requests
from bs4 import BeautifulSoup
import os
import img2pdf


DIRECTORY = "./project_3/data"
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",

# }
# for i in range(1, 49):
#     response = requests.get(f"https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg", headers=headers)
#     if response.status_code == 200:
#         with open(f"./project_3/data/0{i}.jpg", "wb") as file:
#             file.write(response.content)
#     print(f"Iterations: {i}/48")
img = []
for name in os.listdir(DIRECTORY):
    path = os.path.join(DIRECTORY, name)
    img.append(path)

# print(os.listdir("media"))
# img_list = [f"./project_3/data/{i}.jpg" for i in range(1, 49)]

# for roots, dirs, files in os.walk(DIRECTORY):
#     for name in files:
#         if name == "0":
#             os.rename(DIRECTORY + "/" + name, DIRECTORY + "/0" + name)
with open("./project_3/data/result.pdf", "wb") as file:
    file.write(img2pdf.convert(sorted(img)))

