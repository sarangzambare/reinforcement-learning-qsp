


# The following is the arrangement of states (Bang-bang protocol)



#       0  2  4  6  8
#       -  -  -  -  -    h=+2

#       -  -  -  -  -    h=-2
#		1  3  5  7  9



import numpy as np
import random
from scipy import linalg


def ground_state(ham):

	eig, eig_v = linalg.eig(ham)
	a,b = eig

	if(a<b):
		return eig_v[:,0]

	elif(a>b):
		return eig_v[:,1]
	else:
		print "Error: Eigen values fishy"



def reward(current_state,t):

	if(t<(T-1)):
		return 0
	elif(t==(T-1)):
		return abs(current_state.dot(final_state))**2
	else:
		print "Time exceeded ramp time"
		sys.exit(0)


def evolve(current_state,ham,dt):

	return linalg.expm((-1j)*ham*dt).dot(current_state)


def getX(state):
	return state.dot(Sx.dot(state))




T = 10		#total ramp time
dt = 1 		#time step size
alpha = 0.2 #learning rate

Sx =   np.array([[0,0.5],[0.5,0]])
Sz =   np.array([[0.5,0],[0,-0.5]])
up =   np.array([1,0])
down = np.array([0,1])

pos_ham = -Sz + 2*Sx
neg_ham = -Sz - 2*Sx


start_state = ground_state(pos_ham)
final_state = ground_state(neg_ham)



s = ((2*T/dt),2)
Q = np.zeros(s)			# initialising the Q-table to zeroes

EPISODES = 500
random.seed(9030)


class Qubit:
	"Class for representing a single Qubit"

	def __init__(self,theta,phi):
		self.theta = theta
		self.phi = phi
		self.alpha = complex(cos(theta/2))
		self.beta = complex(sin(theta/2)*cos(phi),sin(theta/2)*sin(phi))
		self.vector = [alpha,beta]


class Operator:
	"Class for representing operators, in this case we have 2D space, so we have 2x2 matrix as operator, a and d are diagonal, b and c are off-diagonal"

	def __init__(self,a,b,c,d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d


class State:
	"Class for representing a Q-learning state, here we use time and the corresponding instanteneous magnetic field to represent a state"

	def __init__(self,t,H):
		self.t = t
		self.H = H


delta_t = 0.1
delta_H = 0.1
TOTAL_TIME = 5;


def Q(state,action):
	"Standard Q-Learner reward function"

	print "state.t is %f" % state.t






current_episode = 0
while(current_episode < EPISODES):
	t=0
	state=0
	current_qstate=start_state

	while(t<(T-1)):

		rand = random.random()
		#print "rand is %f" % rand
		if(rand<0.5):
			next_state = state+2 if (state%2==0) else state+1
			#print "time is %d and reward is %f" % (t , reward(evolve(current_qstate,pos_ham,dt),t+dt))
			Q[state,0] = reward(evolve(current_qstate,pos_ham,dt),t+dt) + 0.2*max(Q[next_state,0],Q[next_state,1])
			t+=dt
			current_qstate = evolve(current_qstate,pos_ham,dt)
			state = next_state

		else:
			next_state = state+3 if (state%2==0) else state+2
			#print "time is %d and reward is %f" % (t,  reward(evolve(current_qstate,neg_ham,dt),t+dt))
			Q[state,1] =  reward(evolve(current_qstate,neg_ham,dt),t+dt) + 0.2*max(Q[next_state,0],Q[next_state,1])
			t+=dt
			current_qstate = evolve(current_qstate,neg_ham,dt)
			state=next_state

	current_episode+=1


print Q

print "\n"
print "#T, H"
print "0, 2"
current_qstate=start_state
state=0
t=0
while((t+1)<T): 				#while(state!=((2*T/dt)-1) or state!=((2*T/dt)-2) ):

	if(Q[state,0]>=Q[state,1]):
		print "%d , %d" % (t+1,2)
		current_qstate = evolve(current_qstate,pos_ham,dt)
		state = state+2 if (state%2==0) else state+1
		#print "state is %d" % state
		t+=dt
	else:
		print "%d, %d" % (t+1,-2)
		current_qstate = evolve(current_qstate,neg_ham,dt)
		state = state+3 if (state%2==0) else state+2
		#print "state is %d" % state
		t+=dt



print "Fidelity is %f" % abs(current_qstate.dot(final_state))**2
