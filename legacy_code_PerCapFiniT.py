# prompt: Use the simpy package to generate the Lotka-Volterra model used above to display the mathematical equations. No need to solve them.

import simpy

# Define the model
model = simpy.Environment()

# Define the parameters
r = 1
a = 0.5
c = 0.1
m = 2

# Define the states
B = simpy.Container(model, initial_value=10)
P = simpy.Container(model, initial_value=10)

# Define the processes
def growth(env, b, p):
  while True:
    yield env.timeout(1)
    b.level += r * b.level

def predation(env, b, p):
  while True:
    yield env.timeout(1)
    b.level -= a * b.level * p.level

def burst(env, b, p):
  while True:
    yield env.timeout(1)
    p.level += c * a * b.level * p.level

def death(env, p):
  while True:
    yield env.timeout(1)
    p.level -= m * p.level

# Run the simulation
model.run(until=10)

# Print the results
print(B.level)
print(P.level)
