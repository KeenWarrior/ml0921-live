import gym
import numpy as np
env = gym.make('CartPole-v0')

env.reset()

action = 0

# print(dir(env.unwrapped))
print(env.unwrapped.state)

for i in range(1000):

    if env.unwrapped.state[0] > 0:
        env.step(0)
    else:
        env.step(1)

    action = (action + 1) % 2


    env.render()
