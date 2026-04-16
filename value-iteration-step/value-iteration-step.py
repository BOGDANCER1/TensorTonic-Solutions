import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    old_values = values.copy()
    
    for i in range(len(values)):
        # Compute transition_rewards = transitions[i] @ old_values
        # transitions[i] is a matrix, so we need to multiply matrix by vector
        transition_rewards = []
        for row in transitions[i]:
            # Dot product of row with old_values
            dot_product = 0
            for j in range(len(old_values)):
                dot_product += row[j] * old_values[j]
            transition_rewards.append(dot_product)
        
        # Compute compete_reward = gamma * transition_rewards + rewards[i]
        # rewards[i] is a vector (or list)
        compete_reward = []
        for j in range(len(transition_rewards)):
            compete_reward.append(gamma * transition_rewards[j] + rewards[i][j])
        
        # values[i] = np.max(compete_reward)
        values[i] = max(compete_reward)
    
    return values
        