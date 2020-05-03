import pandas as pd

agent_1 = 0
agent_2 = 0
agent_3 = 0
agent_4 = 0

df = pd.read_csv(r'hearts.csv')


def convert_to_int(score):
    # print(score.strip('[').strip(']'))
    temp1_score = score.strip('[').strip(']')
    temp2_score = temp1_score.replace(',', ' ')
    list_of_ints = [int(s) for s in temp2_score.split() if s.isdigit()]
    return list_of_ints


def get_max_score(score):
    print(score)
    m_score = max(score)
    m_score_index = score.index(max(score))
    return m_score, m_score_index


for key, value in df.iterrows():
    game_score = convert_to_int(value['score'])
    max_score, max_index = get_max_score(game_score)

