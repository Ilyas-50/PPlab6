def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

filename = "example.txt" 
lines_count = count_lines(filename)
print(lines_count)
