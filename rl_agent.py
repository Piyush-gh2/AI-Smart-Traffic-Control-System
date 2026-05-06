import numpy as np

actions = ["Reduce", "Normal", "Increase"]

Q = np.zeros((3, 3))

def choose_action(state):
    return np.argmax(Q[state])

def update_q(state, action, reward, next_state):
    lr = 0.1
    gamma = 0.9
    
    Q[state, action] = Q[state, action] + lr * (
        reward + gamma * np.max(Q[next_state]) - Q[state, action]
    )

def get_state(vehicles):
    if vehicles < 30:
        return 0
    elif vehicles < 80:
        return 1
    else:
        return 2