import cv2
import os


def image_resizer(path, width: int = 640, height: int = 480):
    """
    Image resizing function
    :param path: Path of the image dir
    :param width: Image width
    :param height: Image height
    :return: None
    """
    if not os.path.exists(path="Resized Images"):
        os.mkdir(path="Resized Images")
    all_img = os.listdir(path=path)
    # print(all_img)
    for img in all_img:
        main_img = cv2.imread(filename=os.path.join(path, img))
        resized_img = cv2.resize(src=main_img, dsize=(width, height))
        cv2.imwrite(filename=f"Resized Images\\{img}", img=resized_img)
    print("Successfully Done")


image_resizer(path="Image")
