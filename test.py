import pybullet as pb
from time import sleep
import pybullet_data
physicsClient = pb.connect(pb.GUI)


pb.setAdditionalSearchPath(pybullet_data.getDataPath())
planeID = pb.loadURDF("plane.urdf")

#for this test.py let us load only the slider and check if it works
hopperID = pb.loadURDF("slider_test.urdf")
#only slider opens up but we get simulation for a very short time.
for i in range(100):
    pos, ori = pb.getBasePositionAndOrientation(hopperID)
    pb.stepSimulation()





