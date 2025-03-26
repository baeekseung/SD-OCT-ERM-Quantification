import os
import glob
from PIL import Image

def crop_png_files(src_dir, dest_dir, crop_area):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    cropped_files_count = 0  # 잘린 파일의 개수를 저장할 변수 추가

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.png'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                with Image.open(src_file) as img:
                    crop_img = img.crop(crop_area)
                    crop_img.save(dest_file, 'PNG')
                cropped_files_count += 1  # 파일이 잘릴 때마다 카운트 증가

    return cropped_files_count  # 잘린 파일의 개수를 반환


source_path = "./RawData_png"
destination_path = "./SD-OCT"
crop_area = (496,0,1264,496)  # 자를 영역 (left, upper, right, lower)
cropped_count = crop_png_files(source_path, destination_path, crop_area)
print(f"잘린 png 파일의 개수: {cropped_count}")
