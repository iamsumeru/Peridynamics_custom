import numpy as np

# Import peri module
from peri.simulation import session as sess

# Create session object
s1 = sess.run(name='2DSheet_with_inclusions')
s1.show_graph=False
#Input RVE dimensions
r_x=int(input("Enter Lx "))
r_y=int(input("enter Ly "))
# Define cuboidal block (resolution is slightly larger than Lz => one particle thick sheet => 2D)
prop =  {'Lx': r_x,'Ly': r_y, 'Lz': 0.009, 'res': 0.01, 'id': 1, 'center': [0, 0, 0]} # id = 1 for 2DSheet (matrix)
type = 'cuboid'

# Define sub objects (inclusions)
sub_objs_inner = []
sub_objs_outer = []

#Pre-setting inclusions
area_box=float(prop['Lx']*prop['Ly']*prop['Lz'])
#tar_vf=input("Enter target volume fraction ")
#net_area_incl=float(tar_vf)*area_box/100.0
d_fif=input("Enter d50 (radius) ")
#area_incl=float(np.pi*pow(float(d_fif),2)/4)
#no_incl=int(net_area_incl/area_incl)
asp_r=input("Enter aspect ratio ")

#Pre-defined inclusions
#area_box=float(prop['Lx']*prop['Ly']*prop['Lz'])
num_incl=int(input("enter number of inclusions "))

data = np.loadtxt('./incl_list.txt')
x = data[:,0]
y = data[:,1]

# Creating 100 inclusions with random position and orientation
for i in range(num_incl):
    # center of elliptical inclusion
    h= x[i]-1.5 #float(input("enter x co-ordinate for inclusion "+str(i+1)))-1.5
    k= y[i]-1.5 #float(input("enter y co-ordinate for inclusion "+str(i+1)))-1.5
    # rotation angle of ellipticle inclusion
    A=0#float(input("enter orientation for inclusion "+str(i+1)))
    # length parameter of ellipse
    a = 0.3
    b = 0.3
    # Standard ellipse equation with random center(h,k) and rotated by angle A passed as logical statement (see "<" sign).
    #((x-h)*cos(A)+(y-k)*sin(A))^2/a^2 + ((x-h)*sin(A)-(y-k)*cos(A))^2/b^2 < 1
    logi_outer = '((x-{0})*{4}+(y-{1})*{5})**2/({2}**2) + ((x-{0})*{5}-(y-{1})*{4})**2/({3}**2) < 1.1378'.format(h,k,a,b,np.cos(A),np.sin(A))
    logi_inner = '((x-{0})*{4}+(y-{1})*{5})**2/({2}**2) + ((x-{0})*{5}-(y-{1})*{4})**2/({3}**2) < 1'.format(h,k,a,b,np.cos(A),np.sin(A))

    # store all sub objects (inclusions) as python list.
    sub_objs_inner.append({'logical':logi_inner,'id':2})  # id = 2 for inclusions
    
    sub_objs_outer.append({'logical':logi_outer,'id':3})  # id = 3 for inclusions
    
# Create object as defined above with sub_objs (inclusions)
s1.add_object(name='2Dsheet',type=type,prop=prop, sub_objs=sub_objs_outer+sub_objs_inner, SO_node_list=False)

# Create data matricx
s1.create_data()
s1.assemble_data()

# Define node list using logical expression
#s1.add_node_list(name='right_end', objects=[],logical='x>=1.495') # right most edge (width 10)
#s1.add_node_list(name='left_end', objects=[],logical='x<=-1.495') # left most edge (width 10)
#s1.add_node_list(name='top_end', objects=[],logical='y>=1.495') # right most edge (width 10)
#s1.add_node_list(name='bottom_end', objects=[],logical='y<=-1.495') # left most edge (width 10)
# Write node list to files
s1.write_node_lists()

# Write matrix data to file (input data file for peridigm remove first two line if required)
s1.write_data()

# Write matrix data to file (id based on node list for easy visualization )
s1.write_data_node_list()
