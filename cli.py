# cli.py
"""

Python cli to get food trucks in San Francisco and map its location

python cli.py trucks tacos
python getmap <location id> found from the previous step
Example:
python3 cli.py getmap  1656405


"""
import sys
import os
import pandas as pd
import click
import folium

#CSV file as input
csv_file = 'Mobile_Food_Facility_Permit.csv'

def get_df_csv(csv_file):
    """returns dataframe from passed csv file path"""

    # Read data from CSV file
    try: 
        df = pd.read_csv(csv_file)
    except IOError:
        raise "Not able to open file"
    
    return df

def get_map_desc_from_locid(df,locid):
    """ Returns latitude and langitude given location id passed in the df
    """

    # get row from loc id
    result = df.loc[df['locationid'] == int(locid)]
   
    if result.empty:
        raise Exception(f"location id {locid} not found")

    latitude = float(result.Latitude)
    longitude = float(result.Longitude)
    # create a description to be used by html map
    locdescription = result.Applicant + "-" + result.FacilityType

    return (latitude,longitude,locdescription)

@click.group()
def cli():
    """A simple CLI to find food trucks."""
    pass

@cli.command()
@click.argument('locid')
def getmap(locid):
    """Returns - opens in a browser-  location map given location id passed"""

    # open the csv file with data
    df = get_df_csv(csv_file)
    
    # get langitude, longitude and locdescription
    latitude,longitude,locdescription = get_map_desc_from_locid(df,locid)
    
    # Create a map centered around the location
    m = folium.Map(location=[latitude,longitude], zoom_start=15)

    # Add a marker 
    folium.Marker([latitude,longitude],
                popup= locdescription.values[0]).add_to(m)

    # Save the map to an HTML file
    html_file = "map.html"
    m.save(html_file)
    os.system(f"open {html_file} ")


@cli.command()
@click.argument('food_item')
def trucks(food_item):
    """Returns all trucks selling the specified food item."""
    
    # open csv
    df = get_df_csv(csv_file)

    # Filter trucks based on the specified food item
    matching_trucks = df[df['FoodItems'].str.contains(food_item, case=False, na=False)]
    # filter rows with trucks only 
    matching_trucks = matching_trucks[matching_trucks['FacilityType'].str.contains('truck', case=False, na=False)]
    # Remove columns status where is still 'requested' - expired and approved might be good
    matching_trucks = matching_trucks[~matching_trucks['Status'].str.contains('requested', case=False, na=False)  ]

    # locationid,Applicant,FacilityType,cnn,LocationDescription,Address,blocklot,block,lot,permit,Status,FoodItems,X,Y,Latitude,Longitude,Schedule,dayshours,NOISent,Approved,Received,PriorPermit,ExpirationDate,Location,Fire Prevention Districts,Police Districts,Supervisor Districts,Zip Codes,Neighborhoods (old)

    if matching_trucks.empty:
        click.echo(f"No trucks found selling {food_item}.")
        sys.exit(1)
   
    for index, truck in matching_trucks.iterrows():
            click.echo(f"Location ID: {truck['locationid']}")
            click.echo(f"Location: {truck['LocationDescription']}")
            click.echo(f"Address: {truck['Address']}")
            click.echo(f"Zip : {truck['Zip Codes']}")
            click.echo(f"Food Items: {truck['FoodItems']}")
            
            click.echo("----")

if __name__ == '__main__':
    cli()

