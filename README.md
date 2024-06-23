# Food Truck Finder CLI

A simple CLI application to find food trucks based on the food items they offer and display their location on map. This tool reads data from a CSV file and allows users to filter and display information about food trucks selling specific food items.

## Features

- Search for food trucks selling a specified food item.
- Display detailed information about the food trucks, including their location, address, and food items they offer.

## Requirements

Install dependencies:
```
pip install -r requirements.txt
```

  

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/food-truck-finder-cli.git
    cd food-truck-finder-cli
    git clone git@github.com:bandeep2000/foodtrucksf.git
    cd foodtrucksf
    ```

2. **Install the dependencies**:

    ```sh
    pip install pandas click
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

```sh
python cli.py trucks [FOOD_ITEM]
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
### Running the CLI to find on the map

```

python3 cli.py getmap <location id>

*Note*: you can get location id from the above previous command

Example:
python3 cli.py getmap 848080

This will automatically open browser with location - file map.html

```

