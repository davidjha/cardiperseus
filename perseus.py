import pandas as pd
from hearts_agents import hearts_agents

df = pd.read_csv(r'de_randomized_hearts.csv')


def convert_to_int(score):
    """
    Converts the score, a string, into a list of integers.
    :param score: a string ie "[9, 21, 88, 10]"
    :return:
    """
    temp1_score = score.strip('[').strip(']')
    temp2_score = temp1_score.replace(',', ' ')
    list_of_ints = [int(s) for s in temp2_score.split() if s.isdigit()]
    return list_of_ints


def get_max_score(score):
    """
    Returns the max score from a list of ints, and the index of this max score.

    :param score: a list of ints
    :return: m_score, m_score_index
    """
    m_score = max(score)
    m_score_index = score.index(max(score))
    return m_score, m_score_index


def find_agent(agent_list, index, record_result):
    # agent_list = [agent1, agent2, agent3, agent4]
    for i, agent in enumerate(agent_list):
        if i == index:
            if record_result:
                hearts_agents[i]['losses'] += 1
            return agent


def find_average_points():
    pass


def get_worst_player():
    for key, value in df.iterrows():
        game_score = convert_to_int(value['score'])
        max_score, max_index = get_max_score(game_score)
        # worst_agent = find_agent(value['agent1'], value['agent2'], value['agent3'], value['agent4'], max_index, True)
        worst_agent = find_agent(df[['agent1', 'agent2', 'agent3', 'agent4']], max_index, True)
        print(game_score, max_score, worst_agent, max_index)





