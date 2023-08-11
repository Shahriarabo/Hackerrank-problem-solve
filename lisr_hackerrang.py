def process_commands(commands):
    list = []

    for command in commands:
        parts = command.split()
        operation = parts[0]

        if operation == "insert":
            i = int(parts[1])
            e = int(parts[2])
            list.insert(i, e)
        elif operation == "print":
            print(list)
        elif operation == "remove":
            e = int(parts[1])
            list.remove(e)
        elif operation == "append":
            e = int(parts[1])
            list.append(e)
        elif operation == "sort":
            list.sort()
        elif operation == "pop":
            list.pop()
        elif operation == "reverse":
            list.reverse()

# Take input for the number of commands
num_commands = int(input("Enter the number of commands: "))

# Take input for each command and store them in a list
input_commands = []
for _ in range(num_commands):
    input_commands.append(input())

process_commands(input_commands)
