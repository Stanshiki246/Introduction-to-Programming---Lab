# Stanley Tantysco - 2201814670
# Make a projectile motion program
# Import matplotlib built-ins
import matplotlib.pyplot as plt
# Import numpy built-ins
import numpy as np
# Variable for inputting number of trajectories
tr = int(input("Number of trajectories: "))
# Variable for looping
count = 1
# Start the looping
while count <= tr:
    # Variable for inputting velocity
    v = int(input("Input velocity: "))
    # Variable for acceleration
    a = 9.8
    # Variable for inputting angle
    n=int(input("Input angle: "))
    count += 1
    # Variable for maximum time
    tmax=2*(v*np.sin(np.radians(n))/a)
    # Variable for time graphic line
    timemat =np.linspace(0,tmax,100)
    # Variables for distance and velocity
    x1=[]
    y1=[]
    # Looping for adding data into x1 and y1
    for k in timemat:
        # Variable for distance formula
        x = ((v*k)*np.cos(np.radians(n)))
        # Variable for velocity formula
        y = ((v*k)*np.sin(np.radians(n))) - ((0.5*a)*(k**2))
        x1.append(x)
        y1.append(y)
    # Make x label of distance
    plt.xlabel("Distance")
    # Make y label of velocity
    plt.ylabel("Velocity")
    # Make data plot
    plt.plot(x1,y1,label="Velocity: {} m/s Angle: {}".format(v,n))
# Make legend mappings of velocity and angle
plt.legend()
# Show data plot
plt.show()
