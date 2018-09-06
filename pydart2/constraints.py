from __future__ import absolute_import
# from builtins import object
# Copyright (c) 2015, Disney Research
# All rights reserved.
#
# Author(s): Sehoon Ha <sehoon.ha@disneyresearch.com>
# Disney Research Robotics Group
from . import pydart2_api as papi


class BallJointConstraint(object):
    def __init__(self, body1, body2, jointPos):
        self.body1 = body1
        self.body2 = body2
        self.jointPos = jointPos

    def add_to_world(self, world):
        papi.addBallJointConstraint(world.id,
                                    self.body1.skid,
                                    self.body1.id,
                                    self.body2.skid,
                                    self.body2.id,
                                    self.jointPos)

class HumanArmJointLimitConstraint(object):
    def __init__(self, shldJoint, elbowJoint, mirror):
        self.shldJoint = shldJoint
        self.elbowJoint = elbowJoint
        self.mirror = mirror
        
    def add_to_world(self, world):
        if hasattr(papi, 'addHumanArmJointLimitConstraint'):
            papi.addHumanArmJointLimitConstraint(world.id,
                                             self.shldJoint.skid,
                                             self.shldJoint.id,
                                             self.elbowJoint.id,
                                             self.mirror)

class HumanLegJointLimitConstraint(object):
    def __init__(self, thighJoint, shinJoint, ankleJoint, mirror):
        self.thighJoint = thighJoint
        self.shinJoint = shinJoint
        self.ankleJoint = ankleJoint
        self.mirror = mirror
    
    def add_to_world(self, world):
        if hasattr(papi, 'addHumanLegJointLimitConstraint'):
            papi.addHumanLegJointLimitConstraint(world.id,
                                             self.thighJoint.skid,
                                             self.thighJoint.id,
                                             self.shinJoint.id,
                                             self.ankleJoint.id,
                                             self.mirror)
