import cv2

image_path = input("Enter the path to your image: ")
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image.")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

choice = input("What do you want to do ??\n type 'show' to display the image.\n type 'save' to save the image.\n type 'exit' to exit.\n").strip().lower()
# "strip()" removes the leading and trailing spaces from a word.
# "lower()"" converts the string to lowercase.

if choice == 'show':
    cv2.imshow('Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif choice == 'save':
    save_name = input("Enter the name you want to save the image with: ")
    cv2.imwrite(save_name, gray_image)
    print(f"Image saved as {save_name}")
elif choice == 'exit':
    print("Exiting the program.")