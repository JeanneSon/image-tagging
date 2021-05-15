from os import listdir as ls
from PIL import Image as pil_image
import piexif
from IPython.display import Image, clear_output
SKIPPER = "next"
INTERRUPTOR = "quit"
ABORT_INFO = "Tags: [to skip enter '" + SKIPPER + "'; to quit enter '" + INTERRUPTOR + "'] "
CONFIRMER = "y"
REDO = "rewrite"

def confirm(msg, confirming_c=CONFIRMER):
    response = input(msg)
    return response.strip().lower()

def array_to_tuple(a):  #a stands for array
    result = []
    for word in a:
        word_array = []
        for c in word: #c stands for character
            word_array += [ord(c), 0]
        word_array += [ord(";"), 0]
        result += word_array
    result += [0, 0]
    return tuple(result)

def save_with_new_exif(file, tag_tuple):
    im = pil_image.open(file)
    exif_dict = piexif.load(file)
    exif_dict["0th"][40094] = tag_tuple
    exif_bytes = piexif.dump(exif_dict)
    im.save(file, exif=exif_bytes)
    
def tag_input():
    return confirm("Save these tags? [y/n/rewrite] ")
    
def show_and_treat(file):
    display(Image(file,width=300))
    confirm = REDO
    while (confirm == REDO):
        tag_input_string = input(ABORT_INFO).strip()
        if tag_input_string == SKIPPER:
            return
        if tag_input_string == INTERRUPTOR:
            return True
        tag_array = tag_input_string.split(" ")
        print(tag_array)
        confirm = tag_input()
        if confirm == CONFIRMER:
            tag_tuple = array_to_tuple(tag_array)
            save_with_new_exif(file, tag_tuple)
        

def add_label_to_pictures(directory):
    for file in ls(directory):
        print(file)
        if file.lower().endswith("jpg") or file.lower().endswith("jpeg"):
            complete_filename = directory + "/" + file
            if (show_and_treat(complete_filename)):
                return
            clear_output()
        
def loop_over_pictures():
    keep = True
    while (keep):
        add_label_to_pictures(find_directory("C:\\Users\\HScha\\Pictures"))
        keep = input("Continue tagging? [y]").strip()
        keep = True if keep == "y" else False
#add_label_to_pictures(".")
