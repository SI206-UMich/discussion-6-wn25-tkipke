import unittest
import os
import csv


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''

    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)
    # use this 'full_path' variable as the file that you open

    with open(full_path, 'r') as f:
        r = csv.reader(f)
        rows = []
        print("Add data from csv")
        for row in r:
            rows.append(row)
            print(f"Adding {row} to rows")
        # print(f"Rows: {rows}")
    d = {}

    headers = rows[0][1:]
    print(f"Headers: {headers}")

    for header in headers:
        d[header] = {}
        for row in rows[1:]:
            d[header][row[0]] = row[1:]
    print(d)
        

def get_annual_max(d):
    '''
    Params:
        d, dict created by load_csv above

    Returns:
        list of tuples, each with 3 items: year (str), month (str), and max (int) 
        max is the maximum value for a month in that year, month is the corresponding month

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary.
        You'll have to change vals to int to compare them. 
    '''

    print(d)

    pass

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    pass

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', 628))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")


if __name__ == '__main__':
    main()
