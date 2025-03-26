import os
import shutil

def copy_bmp_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    copied_files_count = 0  # 복사된 파일의 개수를 저장할 변수 추가

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.bmp') and file not in ['0.bmp', '1.bmp']:
                src_file = os.path.join(root, file)
                # 파일명을 숫자로 변경하여 저장
                dest_file = os.path.join(dest_dir, f"{copied_files_count}.bmp")
                shutil.copy2(src_file, dest_file)
                copied_files_count += 1  # 파일이 복사될 때마다 카운트 증가

    return copied_files_count  # 복사된 파일의 개수를 반환


source_path = "./SourceData"
destination_path = "./SD-OCT_bmp"
copied_count = copy_bmp_files(source_path, destination_path)
print(f"복사된 bmp 파일의 개수: {copied_count}")
