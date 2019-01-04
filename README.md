# Reinforcement learning for quantum state preparation
## Author: Sarang Zambare

This repository is a part of a project I undertook at the *Indian Institute of Technology, Bombay*. I demonstrate a basic way in which reinforcement learning can be used to prepare a given quantum state, from a given initial state.

In this particular demonstration, I keep things simple and assume that the quantum state in question is a two level system, and an arbitrary state can be represented as :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/state.png)

To transform the state from one to the other, I use the [bang-bang protocol](https://en.wikipedia.org/wiki/Bang%E2%80%93bang_control), also known as hysteresis control or 2-state control in control theory, to switch between two hamiltonians being operated to the quantum state at each time instant. The two hamiltonians I used are the ground state hamiltonians given by:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/hamiltonians.png)

The control parameter that I use is the magnetic field, which can be +2 or -2 (this is also the coefficient of Sx in the hamiltonians)

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/hamiltonian_2.png)

where h(t) is the magnetic field and the control parameter.


### Formulation of the problem :

The problem of finding the right choice of h(t) so as to prepare the target state, has to be modelled in a way that is compatible with the Q-learning requirements. Therefore, we need to define states, actions, rewards and the Q-matrix. Suppose we have to prepare the state in time T, and our smallest time step is dt, then for every time step dt, we have the option of keeping the magnetic field as +2 or  2. Therefore, we define a state by the couple

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/states_2.png)

Where S denotes the set of states.

For every possible time t , we have two possible values of the magnetic field, therefore the number of states is :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/no_states.png)


For example, lets say T = 4 and dt = 1, then the states would be depicted as follows:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/states_1.png)

For every state, there are two possible actions, lets call these as **Action 0** and **Action 1**, and they are depicted as follows:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/actions.png)


Every reinforcement learning agent needs a measure of reward which is tries to maximise. In this problem, reward is determined by how close the agent is able to prepare the final state to the intended state. Accordingly, the reward function is determined as :


![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/reward.png)
