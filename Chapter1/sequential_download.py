import urllib.request


def download_image(image_path: str, file_name: str) -> None:
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)


def main():
    for i in range(10):
        image_name = "temp/image-" + str(i) + ".jpg"
        download_image("http://lorempixel.com/400/200/sports", image_name)


if __name__ == '__main__':
    main()

