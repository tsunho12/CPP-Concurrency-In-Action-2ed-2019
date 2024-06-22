import re
import argparse

def replace_underscore(text):
    # 找到所有的 \begin{cpp} ... \end{cpp} 块
    cpp_blocks = [(m.start(), m.end()) for m in re.finditer(r'\\begin{cpp}.*?\\end{cpp}', text, re.DOTALL)]
    
    # 替换不在 \begin{cpp} ... \end{cpp} 块中的 _ 为 \_
    result = []
    last_end = 0
    for start, end in cpp_blocks:
        # 处理 \begin{cpp} 之前的部分
        before_cpp = text[last_end:start]
        result.append(before_cpp.replace('_', r'\_'))
        
        # 处理 \begin{cpp} ... \end{cpp} 部分
        cpp_block = text[start:end]
        result.append(cpp_block)
        
        last_end = end
    
    # 处理最后一个 \end{cpp} 之后的部分
    after_last_cpp = text[last_end:]
    result.append(after_last_cpp.replace('_', r'\_'))
    
    return ''.join(result)

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = replace_underscore(content)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"文件处理完成，结果已保存到 {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace _ with \\_ outside of \\begin{cpp}...\\end{cpp}')
    parser.add_argument('input_file', type=str, help='输入文件名')
    parser.add_argument('output_file', type=str, help='输出文件名')
    
    args = parser.parse_args()
    main(args.input_file, args.output_file)

