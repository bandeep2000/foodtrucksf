
import pytest
import cli
import pandas as pd
from pandas.errors import EmptyDataError

"""
python3 -m pytest -v test_cli.py
"""

def test_delete_file_not_found_error():
    """
    Test that a FileNotFoundError is raised when the file does not exist.
    """
    with pytest.raises(FileNotFoundError) as excinfo:
        cli.get_df_csv("non_existent_file.csv")
    assert str(excinfo.value) == "non_existent_file.csv was not found"

def test_df_invalid_loc_id():
    """
    Test get_map_desc_from_locid function to ensure it raises exception
    """
    mock_data_df = pd.DataFrame([
        {
            "locationid": 735318,
            "Applicant": "Ziaurehman Amini",
            "FacilityType": "Push Cart",
            "LocationDescription": "MARKET ST: DRUMM ST intersection",
            "Address": "5 THE EMBARCADERO",
            "Status": "REQUESTED",
            "FoodItems": "Tacos",
            "Latitude": 37.794331003246846,
            "Longitude": -122.39581105302317
        }
    ])

    
    # test invalid loc id
    # Note 7353181 is invalid id
    with pytest.raises(EmptyDataError) as excinfo:
        # this 
        cli.get_map_desc_from_locid(mock_data_df,7353181)
    assert str(excinfo.value) == "location id 7353181 not found"
