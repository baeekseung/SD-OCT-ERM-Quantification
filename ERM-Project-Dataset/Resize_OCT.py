import os
from PIL import Image

def resize_png_files(src_dir, dest_dir, new_size):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    resized_files_count = 0  # 리사이즈된 파일의 개수를 저장할 변수 추가

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.png'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                with Image.open(src_file) as img:
                    resized_img = img.resize(new_size, Image.LANCZOS)  # 높은 퀄리티로 리사이즈
                    resized_img.save(dest_file, 'PNG')
                resized_files_count += 1  # 파일이 리사이즈될 때마다 카운트 증가

    return resized_files_count  # 리사이즈된 파일의 개수를 반환


source_path = "./SD-OCT"
destination_path = "./SD-OCT_640x640"
new_size = (640, 640)  # 원하는 사이즈 (width, height)
resized_count = resize_png_files(source_path, destination_path, new_size)
print(f"리사이즈된 png 파일의 개수: {resized_count}")
