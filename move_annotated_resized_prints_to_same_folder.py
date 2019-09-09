import os, shutil

ANNOTATED_RESIZED_PRINTS_FOLDER = './resized_prints'
ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER = os.path.join(ANNOTATED_RESIZED_PRINTS_FOLDER, 'final_folder')

if os.path.exists(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER):
    for file in os.listdir(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER):
        os.remove(os.path.join(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER, file))
    os.rmdir(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER)

os.makedirs(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER)


folders = [folder for folder in os.listdir(ANNOTATED_RESIZED_PRINTS_FOLDER) if folder.startswith('V_')]

images = 0
xmls = 0

for i, folder in enumerate(folders):
    print("Folder {}/{}".format(i + 1, len(folders)))
    current_video_folder = os.path.join(ANNOTATED_RESIZED_PRINTS_FOLDER, folder)
    for file in os.listdir(current_video_folder):
        if file.endswith('.jpg'):
            images += 1
        elif file.endswith('.xml'):
            xmls += 1

        if not file.startswith('classes'):
            file_full_path = os.path.join(current_video_folder, file)
            shutil.copy(file_full_path, os.path.join(ANNOTATED_RESIZED_PRINTS_FINAL_FOLDER, '{}_{}'.format(folder, file)))

print("{} images, {} xmls".format(images, xmls))