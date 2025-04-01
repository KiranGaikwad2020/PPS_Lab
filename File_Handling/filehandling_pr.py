def transform_content(content):
    # Replace full stops with commas, swap uppercase and lowercase
    return content.replace('.', ',').swapcase()

def copy_and_transform(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        transformed_content = transform_content(content)

        with open(destination_file, 'w', encoding='utf-8') as dest:
            dest.write(transformed_content)
        
        print(f"File '{source_file}' copied to '{destination_file}' with transformations.")
    
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = "test.txt"  # Change this to your source file
destination_file = "output.txt"  # Change this to your destination file
copy_and_transform(source_file, destination_file)

