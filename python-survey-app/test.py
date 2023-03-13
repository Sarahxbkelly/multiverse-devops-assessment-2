from csv_processor import read_csv

def test_input_is_list():
    #Arrange
    filename = "./results.csv"
    expected_output = list

    #Act
    output = (read_csv(filename))

    #Assert
    assert type(output) == expected_output






