import commands2

from commands.drivetime import DriveTime
from commands.turntime import TurnTime
from commands.armangle import armangle
from subsystems.drivetrain import Drivetrain
from subsystems.arm import Arm


class testauto(commands2.SequentialCommandGroup):
    def __init__(self, drive: Drivetrain, arm: Arm) -> None:
        """
        :param drive:
        :param arm:
        """
        super().__init__()

        self.addCommands(
            armangle(90, arm)
    )