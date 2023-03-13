from csv_processor import read_csv
from remove_duplicate import  remove_duplicates
from main import results
from remove_empty_record import remove_empty_records
from capitalise import capitalise
from validate_field import validate_field

#ticket 1

def test_input_is_list():
    #Arrange
    filename = "./results.csv"
    expected_output = list

    #Act
    output = read_csv(filename)

    #Assert
    assert type(output) == expected_output

def test_input_is_correct():
    #Arrange
    filename = "./results.csv"
    expected_output = ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3']

    #Act
    output = read_csv(filename)
    actual_output = output[0]

    #Assert
    assert actual_output == expected_output

#ticket 2

def test_unique_keys():
    #Arrange
    remove_duplicate = remove_duplicates(results)
    expected_output = 22

    #Act
    output = remove_duplicate

    #Assert
    assert len(output) == expected_output

#ticket 3

def test_remove_blanks():
    #Arrange
    remove_blanks = remove_empty_records(remove_duplicates(results))
    expected_output = 21

    #Act
    output = remove_blanks

    #Assert
    assert len(output) == expected_output

