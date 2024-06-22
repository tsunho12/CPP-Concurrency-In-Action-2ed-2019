import re
import sys

def replace_code_blocks(text):
    # Define the pattern to match content inside triple backticks
    pattern = r"```(.*?)```"

    # Define the replacement function
    def replacement(match):
        content = match.group(1).strip()
        return f"\\begin{{cpp}}\n{content}\n\\end{{cpp}}"

    # Perform the replacement using re.sub with the replacement function
    result = re.sub(pattern, replacement, text, flags=re.DOTALL)

    return result

def main(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Replace the code blocks
    replaced_text = replace_code_blocks(text)

    # Write the replaced content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(replaced_text)

# Ensure the script is being run with two arguments
if len(sys.argv) != 3:
    print("Usage: python replace_code_blocks.py <input_file> <output_file>")
else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
