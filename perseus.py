import pandas as pd
import pprint
from hearts_agents import hearts_agents

df = pd.read_csv(r'de_randomized_hearts.csv')


def convert_to_int(score):
    """
    Converts the score, a string, into a list of integers.
    :param score: a string ie "[9, 21, 88, 10]"
    :return: list_of_ints
    """
    temp1_score = score.strip('[').strip(']')
    temp2_score = temp1_score.replace(',', ' ')
    list_of_ints = [int(s) for s in temp2_score.split() if s.isdigit()]
    return list_of_ints


def find_agent(agent_list, index):
    """
    Returns the agent_id at a given index.

    :param agent_list: list of agents
    :param index: index of the agent
    :return: agent_id
    """

    for i, agent_id in enumerate(agent_list):
        if i == index:
            return agent_id


def find_average_points():
    pass


def compute_number_of_games(agent_id):
    """
    Computes the number of games an agent participated in.

    :param agent_id:
    :return: count
    """
    count = 0
    for key, value in df.iterrows():
        if value['agent1'] == agent_id:
            count = count + 1
        if value['agent2'] == agent_id:
            count = count + 1
        if value['agent3'] == agent_id:
            count = count + 1
        if value['agent4'] == agent_id:
            count = count + 1

        # Save count to hearts_agent dict.
        hearts_agents[agent_id - 1]['games'] = count
    return count


def number_of_games():
    """ Returns total number of games in the dataframe."""
    return len(df.index)


def compute_losses():
    """
    Computes losses of all agents.

    :return: None
    """
    for key, value in df.iterrows():
        # Convert score into a list of ints.
        game_score = convert_to_int(value['score'])

        # Get max score and index
        max_score, max_index = get_max_score(game_score)
        agent_list = [value['agent1'], value['agent2'], value['agent3'], value['agent4']]
        # Find the losing agent.
        worst_agent = find_agent(agent_list, max_index)

        # Save number of losses to hearts_agents dict.
        hearts_agents[worst_agent - 1]['losses'] += 1
        # print(game_score, max_score, worst_agent, max_index)


def get_max_score(score):
    """
    Returns the max score from a list of ints, and the index of this max score.

    :param score: a list of ints
    :return: m_score, m_score_index
    """
    m_score = max(score)
    m_score_index = score.index(max(score))
    return m_score, m_score_index


if __name__ == "__main__":
    compute_losses()
    agent1 = compute_number_of_games(1)
    agent2 = compute_number_of_games(2)
    agent3 = compute_number_of_games(3)
    agent4 = compute_number_of_games(4)
    print(number_of_games())
    pprint.pprint(hearts_agents)
