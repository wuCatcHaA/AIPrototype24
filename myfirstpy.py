import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='brithday user'
        
    )

    parser.add_argument(
        '--name',
        type=str,
        default='Chadarat',
        #required=True,
        help='input the name of people who are using the app'
        
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello world, {who} !!")

def cal_todatVbd(bd):
    birthday = datetime.strptime(bd, '%d-%m-%Y')
    today = datetime.today()
    dayday = today - birthday
    #td = datetime.today().strftime('%d %B %Y')
    return dayday.days

if __name__ == "__main__":
    input_v = parse_input()
    print('this is my first .py file.')
    printHello(input_v.name)
    print(f'you were born {cal_todatVbd(input_v.bd)} days from today')
   
