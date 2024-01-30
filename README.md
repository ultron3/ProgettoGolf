The following program is a demo of what the Golden Golf Tour application will be; It is a multiplatform console program
equipped with a logging system to manage all interactions with the user.

FUNCTIONALITY'

The program is very simple and has 5 features:
- select: display all the database data in a table;
- insert: insert the data;
- delete: I delete the data by entering the record id;
- update: I update the database data;
- exit: close the program;

Please note that this program handles SQL queries safely,
  using parameters instead of directly concatenating user values into SQL strings.
  This helps prevent SQL injection attacks.

EXAMPLE OF USE

Here are some examples of how to use the program's features:

1. **Select:**
    - View all participants in the database.

2. **Insert:**
    - To add a new participant, select the "Insert" option and follow the instructions to enter the required information.

3. **Delete:**
    - Select "Delete" and enter the ID of the participant you want to delete.

4. **Update:**
    - I can change the scores and the club of origin.


5. **Exit:**
    - To close the program, select "Exit".

LOGGINGS

The logging system is a system that allows you to see all interactions with the user when the program is started for the first time
a file is generated, in this case named MWdb.log. From this file I can see:
- INFO
- ERROR
- WARNING
- DEBUG
