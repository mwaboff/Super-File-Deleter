####################
#
# Super Awesome Program Deleter
# by Michael Aboff
# January 2012
#
####################

-----Introduction-----
This program is intended to make things really easy for automated 
deletion of files or folders in Unix (and can work on Windows) operating 
systems. Sorry for this horrible ReadMe, this is my second, maybe.

-----Set Up-----
The program access lists of files/folders that need to be deleted by 
searching for files that contain the file extension (defined in the 
code) either on a server (defined in the code) or in the same directory 
as the the program itself.

The default config file extension is:
.sapd

Each line defines a new file that must be deleted.

An example .emy folder is included with the application that configures 
the program to delete a file called
deleteme.txt
on the user's Desktop.

-----Use-----
Run SuperDeleter.py on the user's computer. If you are going to be 
deleting system files, you may need to run the program as an 
administrator.

Command:
    python SuperDeleter.py

The program first checks to see if the server is available. If it is 
not, then it will check the local directory. If you need to force the 
program to only use the offline files, change the server in to an 
empty string.


