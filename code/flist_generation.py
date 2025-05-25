import os
import glob

train_path = 'DDPM/datasets/traindataimg'
test_path = 'DDPM/datasets/testdataimg'
flist_save_path = 'DDPM/datasets/flist'
file_extensions = ['*.jpg', '*.png', '*.svg', '*.tif']
file_extensions = ['*.jpg', '*.png', '*.svg', '*.tif']
train_files = []
for ext in file_extensions:
    train_files.extend(glob.glob(os.path.join(train_path, ext)))


test_files = []
for ext in file_extensions:
    test_files.extend(glob.glob(os.path.join(test_path, ext)))


os.makedirs(flist_save_path, exist_ok=True)
os.makedirs(flist_save_path, exist_ok=True)

with open('{}/train.flist'.format(flist_save_path), 'w', encoding='utf-8') as f:
    for file_path in train_files:
        f.write(file_path + '\n')
with open('{}/test.flist'.format(flist_save_path), 'w', encoding='utf-8') as f:
    for file_path in test_files:
        f.write(file_path + '\n')