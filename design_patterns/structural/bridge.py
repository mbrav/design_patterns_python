from abc import ABC, abstractmethod, abstractproperty
from dataclasses import asdict, dataclass


@dataclass
class DeviceState:
    volume: float = 0.5
    enabled: bool = False
    channel: int = 1


class Device(ABC):
    """Abstract Device class"""

    @abstractproperty
    def is_enabled(self) -> bool:
        ...

    @abstractmethod
    def enable(self) -> None:
        ...

    @abstractmethod
    def disable(self) -> None:
        ...

    @abstractmethod
    def get_volume(self) -> float:
        ...

    @abstractmethod
    def set_volume(self, volume: float) -> None:
        ...

    @abstractmethod
    def get_channel(self) -> int:
        ...

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        ...


class Remote(Device):
    """Remote class"""

    pass


class Bridge:
    """Bridge class"""

    pass
