import pydart2 as pydart
import numpy as np


if __name__ == '__main__':
    # http://arxiv.org/abs/1709.08685
    print('Example: humanJointLimit')

    pydart.init()
    print('pydart initialization OK')

    world = pydart.World(0.001, './data/skel/kima/kima_human_edited.skel')
    print('MyWorld  OK')

    # enable joint limits
    for skeleton in world.skeletons:
        for jt in range(0, len(skeleton.joints)):
            for dof in range(len(skeleton.joints[jt].dofs)):
                if skeleton.joints[jt].has_position_limit(dof):
                    skeleton.joints[jt].set_position_limit_enforced(True)

    skel = world.skeletons[1]

    leftarmConstraint = pydart.constraints.HumanArmJointLimitConstraint(skel.joint('j_bicep_left'), skel.joint('j_forearm_left'), False)
    rightarmConstraint = pydart.constraints.HumanArmJointLimitConstraint(skel.joint('j_bicep_right'), skel.joint('j_forearm_right'), True)
    leftlegConstraint = pydart.constraints.HumanLegJointLimitConstraint(skel.joint('j_thigh_left'), skel.joint('j_shin_left'), skel.joint('j_heel_left'), False)
    rightlegConstraint = pydart.constraints.HumanLegJointLimitConstraint(skel.joint('j_thigh_right'), skel.joint('j_shin_right'), skel.joint('j_heel_right'), True)
    leftarmConstraint.add_to_world(world)
    rightarmConstraint.add_to_world(world)
    leftlegConstraint.add_to_world(world)
    rightlegConstraint.add_to_world(world)

    pydart.gui.viewer.launch_pyqt5(world)
