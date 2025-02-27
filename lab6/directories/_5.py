def func(filename, my_list):
    with open(filename, 'a') as file:
        for item in my_list:
            file.write(str(item) + '\n')

data = ["Apple", "Banana", "Cherry", "Date", 888]
filename = "output.txt"
func(filename, data)

