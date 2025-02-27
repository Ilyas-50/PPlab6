def copy_file(source, destination):
    with open(source, 'r') as src:
        content = src.read()

    with open(destination, 'w') as dest: 
        dest.write(content)  

source_file = "source.txt"
destination_file = "copy.txt"

copy_file(source_file, destination_file)
