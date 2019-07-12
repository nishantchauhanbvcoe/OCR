#Importing libraries
import pytesseract
import cv2
import time
from PIL import Image
from difflib import SequenceMatcher
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


#To match the percentage equality of input and output
def similar(a,b):
    return (SequenceMatcher(None, a, b).ratio())*100


def __main__():

    #Input the address of image file   
    input_image_choice = input("Do you wanna input image  :\n0 - I have an image \n1 - Pass the default image\n ").strip()
    
    if input_image_choice == "0":
        input_image = input("Address of the Image: ")
        choice = 0
    elif input_image_choice == "1":
        input_image = "C:/Users/dell/Desktop/OCR/test_image.PNG"
        choice = 1
    else:
        print("Invalid Choice! Default Image will be passed.\n")
        input_image = "C:/Users/dell/Desktop/OCR/test_image.PNG"
        choice = 1

    #Reading Image
    input_image = input_image.strip()
    image_read = cv2.imread(input_image)

    #Image Processing:-
    #1. Colored Image will be converted to Gray Image
    colored_to_gray = cv2.cvtColor(image_read , cv2.COLOR_BGR2GRAY)
    ret, gray_to_threshold = cv2.threshold(colored_to_gray, 170, 255, cv2.THRESH_BINARY_INV)

    #Storing the processed image
    filename = "{}.png".format("processed")
    cv2.imwrite(filename, gray_to_threshold)

    #Converting OCR to text using tesseract
    text_OCR = pytesseract.image_to_string(Image.open(filename))

    #Writing o/p to Output.txt file
    output_file = open("Output.txt", "w")
    output_file.write("Text read from image:  %s" % text_OCR)
    output_file.close()

    #Reading the real text from Input.txt
    with open("Input.txt", 'r') as file:
        text_original = file.read().replace('\n', '')

    #OCR text printed
    print(text_OCR)

    #Accuracy printed
    if choice != 0:
        accuracy = similar(text_OCR, text_original)
        print(accuracy)
    else:
        acuuracy_desired = input("Do you wanna find out accuracy of this algorithm:\n0 - Yes(You'll have to enter the input text)\n1 - No")
        if acuuracy_desired == 0:
            text_original = input("Enter the original text:  ")
            accuracy = similar(text_OCR, text_original)
        else:
            print("Ok:(")


#Execution
__main__()

#Delay for 2 seconds
time.sleep(2)





