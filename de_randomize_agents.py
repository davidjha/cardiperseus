import csv
import pandas as pd
import copy
from perseus import convert_to_int

df = pd.read_csv(r'hearts.csv')


def de_randomize():
    """
    De-randomize the agents, and sorts the points (a string) according to the agent. Returns a de-randomized
    ordered list of agents, and list of scores according to this order.

    :return: ordered_game_score, ordered_agents
    """

    ordered_game_score = list()
    ordered_agents = list()
    sorted_game_score = list()
    sorted_agents = list()

    for key, value in df.iterrows():
        # Convert scores list to a list of integers
        game_score = convert_to_int(value['score'])
        agent_list = [value['agent1'], value['agent2'], value['agent3'], value['agent4']]
        temp = list(zip(agent_list, game_score))
        temp.sort()
        #print(temp)

        for agent, score in temp:
            #print(agent, score)
            sorted_game_score.append(score)
            sorted_agents.append(agent)
        # print(sorted_game_score)
        # print(sorted_agents)
        ordered_game_score.append(copy.deepcopy(sorted_game_score))
        ordered_agents.append(copy.deepcopy(sorted_agents))
        sorted_game_score.clear()
        sorted_agents.clear()

    #print(ordered_agents)
    return ordered_game_score, ordered_agents


def write_file(scores, agents):
    """
    Writes the de randomized hearts scores and agents to csv file.
    :param scores: ordered list of scores according to agent positions.
    :param agents: sorted agents list.
    """

    with open('de_randomized_hearts.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(['score', 'agent1', 'agent2', 'agent3', 'agent4'])

    with open('de_randomized_hearts.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\n')
        for i, k in enumerate(scores):
            writer.writerow([scores[i], agents[i][0], agents[i][1], agents[i][2], agents[i][3]])
