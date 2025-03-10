from math import degrees

import commands2
from subsystems import arm

class armangle(commands2.Command):
    def __init__(self, degrees: float, arm: arm) -> None:
        """Creates a new TurnDegrees. This command will turn your robot for a desired rotation (in
        degrees) and rotational speed.

        :param degrees: Degrees to turn. Leverages encoders to compare distance.
        :param arm:   The drive subsystem on which this command will run
        """
        super().__init__()

        self.degrees = degrees
        self.arm = arm
        self.addRequirements(arm)

    def initialize(self) -> None:
        self.arm.setAngle(0)

    def execute(self) -> None:
        self.arm.setAngle(degrees)

    def end(self, interrupted: bool) -> None:
        self.arm.setAngle(degrees)