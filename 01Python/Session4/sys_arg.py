import sys

# Check if at least one command-line argument is provided 
if len(sys.argv) > 1:
    
    script_name = sys.argv[0]
    arguments = sys.argv[1:]
    print(f"File name: {script_name}")
    # Print the command-line arguments
    print("Arguments:")
    for arg in arguments:
        print(arg)
else:
    print("No arguments")
