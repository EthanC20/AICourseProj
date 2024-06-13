import gym
import time

env_name = 'CartPole-v0'
env = gym.make(env_name, render_mode='rgb_array')
state = env.reset()

total_reward = 0
done = False
frames = []
while not done:
    frames.append(env.render())
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    if terminated or truncated:
        done = True
        state = env.reset()
    time.sleep(0.2)
env.close()
print('Total reward Score:', total_reward)

import matplotlib.pyplot as plt
from matplotlib import animation\


def display_frames2video(frames,dpi):
    plt.figure(figsize=(frames[0].shape[0]/dpi, frames[0].shape[1]/dpi), dpi=dpi)
    plt.axis('off')
    patch = plt.imshow(frames[0])
    def animate(frame):
        patch.set_data(frame)
    anim = animation.FuncAnimation(plt.gcf(), animate, frames = frames[1:], interval=50)
    # anim.save('cartpole.mp4')
    anim.save('cartpole.gif', writer='imagemagick')
    print('Movement is saved as cartpole.gif')


display_frames2video(frames, dpi=100)
