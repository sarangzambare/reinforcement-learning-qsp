


# The following is the arrangement of states (Bang-bang protocol)



#       0  2  4  6  8
#       -  -  -  -  -    h=+2

#       -  -  -  -  -    h=-2
#		1  3  5  7  9



import numpy as np
import random
import math
from scipy import linalg


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


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



	if(isclose(t,(T-dt))):

		return abs(current_state.dot(final_state))**2

	else:

		return 0


def evolve(current_state,ham,dt):
	return linalg.expm((-1j)*ham*dt).dot(current_state)




def reconcile(state):			#Multiplies by a phase factor to make coefficient of |0> real
	phase_factor = (state[0].real - 1j*state[0].imag)/math.sqrt(state[0].real**2 + state[0].imag**2)
	return phase_factor*state



def getX(state):
	state = reconcile(state);
	theta = 2*math.acos(state[0].real)
	phi = math.acos((state[1].real)/math.sin(theta/2))

	return math.sin(theta)*math.cos(phi)


def getY(state):
	state = reconcile(state);
	theta = 2*math.acos(state[0].real)
	phi = math.acos((state[1].real)/math.sin(theta/2))

	return math.sin(theta)*math.sin(phi)

def getZ(state):
	state = reconcile(state);
	theta = 2*math.acos(state[0].real)

	return math.cos(theta)





T = 1.0				#total ramp time
dt = 0.1 		    #time step size
alpha = 0.2         #learning rate

Sx =   np.array([[0,0.5],[0.5,0]])
Sz =   np.array([[0.5,0],[0,-0.5]])
Sy =   np.array([[0,-0.5j],[0.5j,0]])
up =   np.array([1,0])
down = np.array([0.0003,0.9999])
trial = 0.707*up + (1j)*0.707*down

pos_ham = -Sz + 2*Sx
neg_ham = -Sz - 2*Sx


start_state = ground_state(pos_ham)
final_state = ground_state(neg_ham)



s = (int(math.ceil(2*T/dt)),2)
Q = np.zeros(s)

EPISODES = 200
random.seed(9030)





current_episode = 0
while(current_episode < EPISODES):
	t=0
	state=0
	current_qstate=start_state

	while(not isclose(t,(T-dt))):
		#print "current t is %f" % t
		rand = random.random()
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
print "0, 2, 0"
current_qstate=start_state
state=0
t=0
index = 1
while((t+dt)<T): 				#while(state!=((2*T/dt)-1) or state!=((2*T/dt)-2) ):

	if(Q[state,0]>Q[state,1]):
		print "%f , %d, %d" % (t+dt,2,index)
		current_qstate = evolve(current_qstate,pos_ham,dt)
		#if(index%2 == 0):
		#	print "Current coordinates are %f, %f, %f" % ((getX(current_qstate),getY(current_qstate),getZ(current_qstate)))
		state = state+2 if (state%2==0) else state+1
		#print "state is %d" % state
		t+=dt
		#index+=1
	elif(Q[state,0]==Q[state,1]):
		rand = random.random()
		if(rand < 0.5):
			print "%f , %d, %d" % (t+dt,2,index)
			current_qstate = evolve(current_qstate,pos_ham,dt)
			#if(index%2 == 0):
			#	print "Current coordinates are %f, %f, %f" % ((getX(current_qstate),getY(current_qstate),getZ(current_qstate)))
			state = state+2 if (state%2==0) else state+1
			#print "state is %d" % state
			t+=dt
			#index+=1
		else:
			print "%f, %d, %d" % (t+dt,-2,index)
			current_qstate = evolve(current_qstate,neg_ham,dt)
			#if(index%2 == 0):
			#	print "Current coordinates are %f, %f, %f" % ((getX(current_qstate),getY(current_qstate),getZ(current_qstate)))
			state = state+3 if (state%2==0) else state+2
			#print "state is %d" % state
			t+=dt
			#index+=1

	else:
		print "%f, %d, %d" % (t+dt,-2,index)
		current_qstate = evolve(current_qstate,neg_ham,dt)
		#if(index%2 == 0):
			#print "Current coordinates are %f, %f, %f" % ((getX(current_qstate),getY(current_qstate),getZ(current_qstate)))
		state = state+3 if (state%2==0) else state+2
		#print "state is %d" % state
		t+=dt
		#index+=1


print "Fidelity is %f" % abs(current_qstate.dot(final_state))**2
