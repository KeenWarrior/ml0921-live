import gym
env = gym.make('CartPole-v0')

env.reset()

env.unwrapped.state = (0, 0, 0, 0)


for i in range(1000):
    response = env.step(i%2)
    print(response)
    env.render()