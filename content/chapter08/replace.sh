#!/bin/bash

# 检查是否提供了输入和输出文件名
if [ "$#" -ne 2 ]; then
	echo "用法: $0 <输入文件> <输出文件>"
	exit 1
fi

input_file="$1"
output_file="$2"

# 使用awk和sed处理文件内容
awk '
/\\begin{cpp}/ {inside_cpp=1} 
/\\end{cpp}/ {inside_cpp=0}
{
    if (inside_cpp) {
        print $0
    } else {
        gsub(/_/, "\_", $0)
        print $0
    }
}
' "$input_file" >"$output_file"

echo "替换完成"
