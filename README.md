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
5. **Plot:**
  - I print the graph with the main ranking points![classifica](https://github.com/ultron3/ProgettoGolf/assets/104757961/f06eb360-ce64-444c-ae81-60943e2ad99b)


6. **Exit:**
    - To close the program, select "Exit".

LOGGINGS

The logging system is a system that allows you to see all interactions with the user when the program is started for the first time
a file is generated, in this case named MWdb.log. From this file I can see:
- INFO
- ERROR
- WARNING
- DEBUG

MODELAI.PY
This file contains a template for data analysis. It connects to the database, takes the total scores and analyzes them to determine the best player.
At the end it prints a graph.
![tensorflow_model](https://github.com/ultron3/ProgettoGolf/assets/104757961/4334cf93-5170-4c5b-a6fc-b2ec9523b5a2)

