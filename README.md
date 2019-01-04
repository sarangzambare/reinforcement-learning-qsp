# Reinforcement learning for quantum state preparation
## Author: Sarang Zambare

This repository is a part of a project I undertook at the *Indian Institute of Technology, Bombay*. I demonstrate a basic way in which reinforcement learning can be used to prepare a given quantum state, from a given initial state.

In this particular demonstration, I keep things simple and assume that the quantum state in question is a two level system, and an arbitrary state can be represented as :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/state.png)

To transform the state from one to the other, I use the [bang-bang protocol](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control), also known as hysteresis control or 2-state control in control theory, to switch between two hamiltonians being operated to the quantum state at each time instant. The two hamiltonians I used are the ground state hamiltonians given by:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/hamiltonians.png)
