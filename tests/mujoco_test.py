import mujoco
import numpy as np

import mujoco.viewer

xml = """
<mujoco>
  <worldbody>
    <geom name="red_box" type="box" size=".2 .2 .2" rgba="1 0 0 1"/>
    <geom name="green_sphere" pos=".2 .2 .2" size=".1" rgba="0 1 0 1"/>
  </worldbody>
</mujoco>
"""

# Load the model from an XML file
model = mujoco.MjModel.from_xml_string(xml)

# Create a data structure to hold the simulation state
data = mujoco.MjData(model)

# Create a viewer to visualize the simulation
viewer = mujoco.viewer.launch_passive(model, data)

# Simulate and render the model
while viewer.is_running():
    mujoco.mj_step(model, data)