import os

path = os.environ['PATH']
print(path)

# Set a new environment variable
os.environ['Test_Variable'] = 'variable 1'


# Get the value of the new environment variable
my_var = os.environ['Test_Variable']
print(my_var)

# Access the "Test_Variable" environment variable
variable_name = "Test_Variable"  
value = os.environ.get(variable_name)


for key, value in os.environ.items():
    print(f"{key}: {value}")
