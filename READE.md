## Instructions

To get tempest to work on your machine, follow the instructions listed below:

- Clone the repo
- Navigate to the project directory in which you cloned the repo
- Activate the python virtual env of your choice.
- Install the required packages with:

  `pip install -r requirements.txt`

- Navigate to the tempest directory with `cd tempest/`

- Create a file called `my.cnf`

- Your `my.cnf` file should look like this:

  ```
  [client]
   database = NAME
   user = USER
   password = PASSWORD
  ```

- Run the following command:

  `python manage.py migrate`

  `python manage.py shell`

- In the interactive shell, run the following commands:

  `from weather.models import ConfigItem`

  `ConfigItem(key = "open weather api key", value = "YOUR OPENWEATHER API KEY").save()`

  `ConfigItem(key = "mapbox api key", value = "YOUR MAPBOX API KEY").save()`

- Exit shell

- Run program with:

  `python manage.py runserver`

- Navigate to `localhost:8000` in your browser.
