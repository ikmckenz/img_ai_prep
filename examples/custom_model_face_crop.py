import cv2
from PIL import Image

from img_ai_prep import img_ai_prep

if __name__ == "__main__":
    im = Image.open(
        "example_photos/original/hugo_leonardo_de_souza_lopez_pixabay.jpg")

    model = cv2.CascadeClassifier(cv2.data.haarcascades +
                                  "haarcascade_frontalface_default.xml")
    newimg = img_ai_prep(im,
                         final_size=1024,
                         crop_mode="face_center_crop",
                         model=model)
    print(newimg.size)
    newimg.save("example_photos/processed/resize_face_center_crop.jpg")
