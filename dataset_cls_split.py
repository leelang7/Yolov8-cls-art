import os
import shutil
from sklearn.model_selection import train_test_split

# 원본 데이터셋 폴더 경로
dataset_folder = "C:\\Users\\admin\\Downloads\\images\\art\\train"

# 이동할 폴더 경로
train_folder = "C:\\Users\\admin\\Downloads\\images\\art\\train\\train"
val_folder = "C:\\Users\\admin\\Downloads\\images\\art\\val"

# 클래스 폴더 목록 생성
class_folders = [folder for folder in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, folder))]

# 각 클래스 폴더의 데이터 이동
for class_folder in class_folders:
    class_folder_path = os.path.join(dataset_folder, class_folder)
    
    # 클래스 폴더 안의 파일 목록 가져오기
    file_list = os.listdir(class_folder_path)
    
    # 훈련 및 검증 데이터로 나누기
    train_files, val_files = train_test_split(file_list, test_size=0.2, random_state=42)
    
    # 훈련 데이터를 train 폴더로 이동
    for file_name in train_files:
        src = os.path.join(class_folder_path, file_name)
        dst = os.path.join(train_folder, class_folder, file_name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
    
    # 검증 데이터를 val 폴더로 이동
    for file_name in val_files:
        src = os.path.join(class_folder_path, file_name)
        dst = os.path.join(val_folder, class_folder, file_name)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
