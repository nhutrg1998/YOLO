# import os
# i = 1
# path = "./Apples/"
# for filename in os.listdir(path): 
#     txtname = path + filename.split('.')[0] + '.txt'
#     f = open(txtname, 'w')
#     f.write("0 0.5 0.5 1 1")
#     f.close()
#     i += 1

import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
current_dir = '/home/cpu11436/Documents/YOLO/Dataset/Apples'
# Percentage of images to be used for the test set
percentage_test = 10
# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')
# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
            counter = 1
            file_test.write("./Dataset/Apples" + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("./Dataset/Apples" + "/" + title + '.jpg' + "\n")
        counter = counter + 1
