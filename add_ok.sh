# 递归遍历所有子目录，但只遍历一层子目录
for dir in $(find . -mindepth 1 -maxdepth 2 -type d); do
    # 遍历子目录下所有的.py文件
    for file in $(find "$dir" -name "*.py"); do
        # 在每个.py文件的第一行添加OK_FORMAT = True
        sed -i '1i OK_FORMAT = True' "$file"
    done
done
