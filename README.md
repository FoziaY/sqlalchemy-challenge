# SQLAlchemy Challenge: Surf's Up!

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_YryYjOrkuljjYeIKy56p3tlDk7jszaRJiBI624NsCqZ8JLdfo8uV2CKWIPXaH05H4fw&usqp=CAU" style="width: 100%; height: auto;">

***
## Background
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. This project involves analyzing and exploring climate data using Python, SQLAlchemy, and Flask.

***

## Instructions
This project consists of two main parts:

### Part 1: Analyze and Explore the Climate Data
Using Python and SQLAlchemy, perform basic climate analysis and data exploration of the climate database.

#### Steps
1. **Database Connection**
    - Use `SQLAlchemy create_engine()` to connect to the SQLite database.
    - Use `SQLAlchemy automap_base()` to reflect the database tables into classes.
    - Save references to the classes named `station` and `measurement`.
    - Link Python to the database by creating a SQLAlchemy session.
    - Ensure to close the session at the end of the notebook.

2. **Precipitation Analysis**

<img src="https://static.bc-edx.com/data/dl-1-2/m10/lms/img/precipitation.jpg" style="width: 100%; height: auto;">

    - Find the most recent date in the dataset.
    - Get the previous 12 months of precipitation data.
    - Load the query results into a Pandas DataFrame and set the column names.
    - Sort the DataFrame by date.
    - Plot the results using the DataFrame plot method.
    - Use Pandas to print the summary statistics for the precipitation data.

4. **Station Analysis**

<img src="https://static.bc-edx.com/data/dl-1-2/m10/lms/img/station-histogram.jpg" style="width: 100%; height: auto;">

    - Calculate the total number of stations in the dataset.
    - Find the most-active stations (stations with the most rows).
    - Calculate the lowest, highest, and average temperatures for the most-active station.
    - Get the previous 12 months of temperature observation data for the most-active station.
    - Plot the results as a histogram with `bins=12`.

### Part 2: Design Your Climate App
Using Flask, design an API based on the queries developed in Part 1.

#### Routes
1. **Homepage `/`**
    - List all available routes.

2. **Precipitation `/api/v1.0/precipitation`**
    - Convert the query results from the precipitation analysis to a dictionary.
    - Return the JSON representation of the dictionary.

3. **Stations `/api/v1.0/stations`**
    - Return a JSON list of stations from the dataset.

4. **Temperature Observations `/api/v1.0/tobs`**
    - Query the dates and temperature observations of the most-active station for the previous year.
    - Return a JSON list of temperature observations for the previous year.

5. **Start `/api/v1.0/<start>` and Start-End `/api/v1.0/<start>/<end>`**
    - Return a JSON list of the minimum, average, and maximum temperature for a specified start or start-end range.

## Requirements
### Part 1: Climate Analysis and Exploration
- **Database Connection (10 points)**
    - Connect to SQLite database.
    - Reflect tables into classes.
    - Save references to classes.
    - Create and close SQLAlchemy session.

- **Precipitation Analysis (16 points)**
    - Query recent date.
    - Query last 12 months of precipitation.
    - Load results into DataFrame.
    - Sort DataFrame by date.
    - Plot results.
    - Print summary statistics.

- **Station Analysis (16 points)**
    - Calculate number of stations.
    - List stations and observation counts.
    - Calculate min, max, and average temperatures for the most-active station.
    - Query last 12 months of temperature observations for the most-active station.
    - Plot results as histogram.

### Part 2: Climate App
- **API SQLite Connection & Landing Page (10 points)**
    - Generate engine for SQLite file.
    - Reflect database schema.
    - Save references to tables.
    - Bind session between Python app and database.
    - Display available routes.

- **API Static Routes (15 points)**
    - Precipitation route: returns JSON of precipitation data for the last year.
    - Stations route: returns JSON of all stations.
    - TOBS route: returns JSON of temperature observations for the most-active station for the last year.

- **API Dynamic Route (15 points)**
    - Start route: returns min, max, and average temperatures from the given start date to the end of the dataset.
    - Start-End route: returns min, max, and average temperatures from the start date to the end date.

### Coding Conventions and Formatting (8 points)
- Place imports at the top of the file.
- Name functions and variables with lowercase characters, using underscores to separate words.
- Follow DRY principles to create maintainable and reusable code.
- Use concise logic and creative engineering.

### Deployment and Submission (6 points)
- Submit a link to a GitHub repository cloned to your local machine.
- Use the command line to add your files to the repository.
- Include appropriate commit messages.

### Comments (4 points)
- Ensure code is well commented with concise, relevant notes.

***

## Usage
To run the analysis:
1. Clone the repository to your local machine.
2. Ensure you have the required libraries installed: `pandas`, `numpy`, `matplotlib`, `sqlalchemy`, `flask`.
3. Add your API keys to the `api_keys.py` file.
4. Open the Jupyter notebook (`climate_starter.ipynb`) and run the cells sequentially.
5. Run the Flask app by executing `python app.py` in the terminal.

***
