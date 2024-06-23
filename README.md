# Food Truck Finder CLI

A simple CLI application to find food trucks based on the food items they offer and display their location on map. This tool reads data from a CSV file and allows users to filter and display information about food trucks selling specific food items.

## Features

- Search for food trucks selling a specified food item.
- Display the information about the food truck on the map



## Installation

1. **Clone the repository**:

    ```
    git clone git@github.com:bandeep2000/foodtrucksf.git
    cd foodtrucksf
    ```

2. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure you have the CSV file**:

    Place your `Mobile_Food_Facility_Permit.csv` file in the same directory as the `cli.py` script. The CSV file should have the following columns:
    - `locationid`
    - `Applicant`
    - `FacilityType`
    - `LocationDescription`
    - `Address`
    - `Status`
    - `FoodItems`
    - `Latitude`
    - `Longitude`

## Usage

### Running the CLI to find food item

To start the CLI, use the following command:

**python cli.py trucks [FOOD_ITEM]**

```sh

Example:

python3 cli.py trucks tacos

Location ID: 848080
Location: RANKIN ST: DAVIDSON AVE to EVANS AVE (200 - 299)
Address: 1700 EVANS AVE
Zip : 58.0
Food Items: Tacos: burritos: quesadillas: combination plates: tortas: tostadas
----
Location ID: 840504
Location: EVANS AVE: QUINT ST to RANKIN ST (1700 - 1799)
Address: 750 PHELPS ST
Zip : 58.0
Food Items: Tacos: burritos: quesadillas: combination plates: tortas: tostadas
----

```
### Running the CLI to find the truck location on the map from location id
**python3 cli.py getmap [Location ID]**

Note: you can get location id from the previous command output for the interested truck

```
Example:

python3 cli.py getmap 848080

This will automatically open browser with location details - map.html

```

