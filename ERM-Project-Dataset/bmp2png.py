import os
from PIL import Image

def convert_bmp_to_png(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    converted_files_count = 0  # 변환된 파일의 개수를 저장할 변수 추가

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.bmp'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, f"{os.path.splitext(file)[0]}.png")
                with Image.open(src_file) as img:
                    img.save(dest_file, 'PNG')
                converted_files_count += 1  # 파일이 변환될 때마다 카운트 증가

    return converted_files_count  # 변환된 파일의 개수를 반환


source_path = "./SD-OCT_bmp"
destination_path = "./SD-OCT_png"
converted_count = convert_bmp_to_png(source_path, destination_path)
print(f"변환된 png 파일의 개수: {converted_count}")
