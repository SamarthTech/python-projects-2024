import pywhatkit as kt

# Display welcome msg
print("Let's convert image to ASCII symbols!")

# Capture source and target path
source_path = "Suzume.png"    # source location
target_path = "ascii_img"   # store location

# Call the 'image_to_ascii_art' method
kt.image_to_ascii_art(source_path, target_path)
