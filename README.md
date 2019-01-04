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


In the above steps, we calculate the state at time (t+dt) by applying the time evolution operator to the state at time t :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/time_evolution_2.png)


When this algorithm is implemented, after many episodes, the Q-matrix thus formed will contain the right choices of magnetic field values at each time step. Keep in mind that the above algorithm is for constructing the Q-matrix only. To discern the optimal choices of fields at every time step, we select the action which has a higher Q-value of the two. If the Q-values are same for the two actions, then it doesn’t matter which action we take, and hence we choose randomly from the two actions.

## Results:

After calculating the value of the magnetic field at every time step, we finally calculate the fidelity of the prepared quantum state :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/fidelity.png)

The Q-learning algorithm mentioned above was implemented using Python. The total ramp time was set to be T = 3 and each time step was dt = 0.1. The learning rate was set to 0.2 and the initial and target quantum states used were the same as mentioned in the previous sections of this report. The values of magnetic field that we used for the bang-bang protocol were ±2. I ran the algorithm for a total of 10,000 episodes, and the **maximum fidelity I achieved was 99.5%**

Any quantum state of a two level system can be represented as a 3D vector on the bloch sphere, where the state can be decomposed as:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/state_complex.png)

and the bloch vector is given by the following components:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/bloch_vector.png)


In this particular example, the start and final state I used can be decomposed as :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/states_start_target.png)

After plotting them on the bloch sphere, they look like so :

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/start_target.png)

After being subjected to the driving protocol that the Q-learning algorithm learned, the maximum fidelity I got was 99.5%. The final prepared state looks like so:

![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/start_target_final.png)


The optimal values of magnetic field at each time step is illustrated in the following figure:


![alt text](https://raw.githubusercontent.com/sarangzambare/reinforcent-learning-qstate-preparation/master/png/optimal_fields.png)
