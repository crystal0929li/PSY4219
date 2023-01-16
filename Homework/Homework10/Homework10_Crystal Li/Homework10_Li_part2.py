import pandas as pd


def exp_summary(test_data):
    """This function reads in study and test csv files and return a summary
       of the experiment hit and false alarms"""
    test_df = pd.read_csv(test_data)
    recognition = test_df[test_df.choice == 'd']
    total_old = len(recognition)

    hits = len(recognition[recognition.ans == 'old'])
    false = len(recognition[recognition.ans == 'new'])

    hit_pro = hits / total_old
    false_pro = false / total_old
    print(f"The proportion of hits is {hit_pro:.2f}.")
    print(f"The proportion of false alarm is {false_pro:.2f}.")


if __name__ == '__main__':
    exp_summary('test_data.csv')
