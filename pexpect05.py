# Import pexpect module

import pexpect
import os


# Run simple command

print("The current working directory: \n%s" %pexpect.run('pwd').decode("utf-8"))


# Retrieve the information of a particular file

filename = input("Enter an existing filename: ")

# Check the file exists or not

if os.path.exists(filename):

    output = pexpect.run("ls -l "+filename, withexitstatus=0)

    print("Information of a particular file: \n%s" %output.decode("utf-8"))

else:

    print("File does not exist.")


# Retrieve the files and folder of a particular directory using ssh command

output = pexpect.run("ssh fahmida@localhost 'ls web/'", events={'(?i)password':'12345\n'})

print("\nThe output of ssh command: \n%s" %output.decode("utf-8"))