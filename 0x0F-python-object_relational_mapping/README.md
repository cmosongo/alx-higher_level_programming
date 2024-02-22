0x0F. Python - Object-relational mapping

Certainly! Let's go through each task and organize the information for a `readme.md` file:

### Task 0: Get all states

**Description:**
Write a script that lists all states from the database `hbtn_0e_0_usa`.

- Script: `0-select_states.py`
- Arguments: mysql username, mysql password, database name
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by states.id
- Output Format: (id, 'state_name')

### Task 1: Filter states

**Description:**
Write a script that lists all states with a name starting with N (upper N) from the database `hbtn_0e_0_usa`.

- Script: `1-filter_states.py`
- Arguments: mysql username, mysql password, database name
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by states.id
- Output Format: (id, 'state_name')

### Task 2: Filter states by user input

**Description:**
Write a script that takes in an argument and displays all values in the states table of `hbtn_0e_0_usa` where name matches the argument.

- Script: `2-my_filter_states.py`
- Arguments: mysql username, mysql password, database name, state name searched
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Query: Use `format` to create the SQL query with the user input
- Results: Sorted in ascending order by states.id
- Output Format: (id, 'state_name')

### Task 3: SQL Injection...

**Description:**
Write a script to display all values in the states table of `hbtn_0e_0_usa` where name matches the argument, safe from MySQL injections.

- Script: `3-my_safe_filter_states.py`
- Arguments: mysql username, mysql password, database name, state name searched (safe from MySQL injection)
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by states.id
- Output Format: (id, 'state_name')

### Task 4: Cities by states

**Description:**
Write a script that lists all cities from the database `hbtn_0e_4_usa`.

- Script: `4-cities_by_state.py`
- Arguments: mysql username, mysql password, database name
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by cities.id
- Output Format: (id, 'city_name', 'state_name')

### Task 5: All cities by state

**Description:**
Write a script that takes the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.

- Script: `5-filter_cities.py`
- Arguments: mysql username, mysql password, database name, state name
- Module: `MySQLdb`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by cities.id
- Output Format: 'city1, city2, city3'

### Task 6: First state model

**Description:**
Create a Python file containing the class definition of a State and an instance `Base = declarative_base()`.

- Script: `model_state.py`
- Class: `State`
  - Inherits from `Base`
  - Links to the MySQL table `states`
  - Attributes: `id` (auto-generated, unique integer), `name` (string with max 128 characters)
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306

### Task 7: All states via SQLAlchemy

**Description:**
Write a script that lists all State objects from the database `hbtn_0e_6_usa`.

- Script: `7-model_state_fetch_all.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by states.id
- Output Format: 'id: state_name'

### Task 8: First state

**Description:**
Write a script that prints the first State object from the database `hbtn_0e_6_usa`.

- Script: `8-model_state_fetch_first.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Output Format: 'id: state_name'

### Task 9: Contains `a`

**Description:**
Write a script that lists all State objects that contain the letter a from the database `h

btn_0e_6_usa`.

- Script: `9-model_state_filter_a.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Results: Sorted in ascending order by states.id
- Output Format: 'id: state_name'

### Task 10: Get a state

**Description:**
Write a script that prints the State object with the name passed as an argument from the database `hbtn_0e_6_usa`.

- Script: `10-model_state_my_get.py`
- Arguments: mysql username, mysql password, database name, state name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Output Format: 'id: state_name' or 'Not found'

### Task 11: Add a new state

**Description:**
Write a script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.

- Script: `11-model_state_insert.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- New State: "Louisiana"
- Print the new State.id after creation

### Task 12: Update a state

**Description:**
Write a script that changes the name of a State object from the database `hbtn_0e_6_usa`.

- Script: `12-model_state_update_id_2.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Update: Change the name of the State with id = 2 to "New Mexico"
- Commit the changes

### Task 13: Delete states

**Description:**
Write a script that deletes all State objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

- Script: `13-model_state_delete_a.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Delete: All states with a name containing the letter `a`

### Task 14: Cities in state

**Description:**
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a City.

- Script: `model_city.py`
- Class: `City`
  - Inherits from `Base`
  - Links to the MySQL table `cities`
  - Attributes: `id` (auto-generated, unique integer), `name` (string with max 128 characters), `state_id` (foreign key to states.id)
- Module: `SQLAlchemy`

### Task 15: City relationship

**Description:**
Write a script that creates the State "California" with the City "San Francisco" from the database `hbtn_0e_100_usa`.

- Script: `100-relationship_states_cities.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Use the cities relationship for all State objects
- New State: "California" with City: "San Francisco"

### Task 16: List relationship

**Description:**
Write a script that lists all State objects, and corresponding City objects, contained in the database `hbtn_0e_100_usa`.

- Script: `101-relationship_states_cities_list.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Display: All State objects and their corresponding City objects
- Sorted by State.id
- Output Format: 'state_name: city_name, city_name'

### Task 17: From city

**Description:**
Write a script that lists all City objects from the database `hbtn_0e_101_usa`.

- Script: `102-relationship_states_cities_list.py`
- Arguments: mysql username, mysql password, database name
- Module: `SQLAlchemy`
- Connection: MySQL server running on localhost at port 3306
- Display: All City objects
- Sorted by City.id
- Output Format: 'city_name: state_name'

