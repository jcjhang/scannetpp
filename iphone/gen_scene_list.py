'''
Generate scene list from a directory of downloaded ScanNet scenes
By frank
'''

import os

# Write the folder names of a directory to a text file
def write_scene_list(dir_path, output_file):
    with open(output_file, 'w') as f:
        for name in os.listdir(dir_path):
            f.write(name + '\n')
            
if __name__ == '__main__':
    SCENE_DATA_DIR = "/media/public_dataset2/ScanNet++_updated/data"
    SCENE_LIST_FILE = "downloaded_scene_list.txt"
    write_scene_list(SCENE_DATA_DIR, SCENE_LIST_FILE)
    print(f"Scene list written to {SCENE_LIST_FILE}")