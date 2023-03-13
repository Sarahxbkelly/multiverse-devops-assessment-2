from csv_processor import read_csv

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




