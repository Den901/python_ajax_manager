"""Ajax System abstract devices."""

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union

from _sha1 import sha1

from ..exceptions import AjaxSystemUnmanagedDeviceError


_LOGGER = logging.getLogger(__name__)


#TYPE_ = #COMPILE WITH NUMBER
#TYPE_ = 
#TYPE_ = 
#TYPE_ = 


TYPES = {
    # Internal types 

    0: "EDITME", #COMMIT ME
    1: "EDITME",
    2: "EDITME",
    3: "EDITME",
    4: "EDITME",
    5: "EDITME",
    6: "EDITME",

}

StateType = Union[None, str, int, float]
DeviceState = Dict[str, Any]


  class AjaxDevice(ABC):
    """AjaxSystem abstract device class."""

    @abstractmethod
    def __init__(
        self,
        manager,
        type_id: int,
        device_info: DeviceState,
        device_class: Optional[str] = "",
    ):
        """Init instance."""
        self._manager = manager
        self._type_id = type_id
        self._device_info = device_info

        self._device_class = device_class if device_class != "" else self.type.lower()

    @property
    def unique_id(self) -> str:
        """Return the unique ID of device."""
        return "-".join(
            [str(self._type_id), sha1(self.name.encode("utf-8")).hexdigest()]
        )

    @property
    def type_id(self) -> int:
        """Return the type ID of device."""
        return self._type_id

    @property
    def type(self) -> str:
        """Return the type of device."""
        return TYPES[self._type_id]

    @property
    def name(self) -> Optional[str]:
        """Return the name of device."""
        return self._device_info.get("name")

    @property
    def act_id(self) -> Optional[int]:
        """Return the action ID for device."""
        return self._device_info.get("act_id")

    def _check_act_id(self):
        """Check for act ID availability."""
        if not self.act_id:
            raise ETIDomoUnmanagedDeviceError()


    @property
    def available(self) -> bool:
        """Return True if device is available."""
        return self._manager.connected

    @property
    def state(self) -> StateType:
        """Return the current device state."""
        return self._device_info.get("status")

    def update_state(self, state: DeviceState) -> bool:
        """Update device state."""
        if state.get("act_id") != self.act_id:
            return False

        if state.get("cmd_name"):#EDIT ME
            state.pop("cmd_name")#EDIT ME

        log = {}
        for k, val in state.items():
            if self._device_info.get(k) != val:
                log[k] = val
        if log:
            _LOGGER.debug(
                'Received new state for %s "%s": %s',
                self.type.lower(),
                self.name,
                log,
            )

        self._device_info = state

        return bool(log)

    def _force_update(self, cmd_base: str, field: str = "array"): #EDIT ME
        """Force update device state."""
        self._check_act_id()

        cmd = {
            "cmd_name": f"{cmd_base}_list_req",
            "topologic_scope": "act",
            "value": self.act_id,
        }
        res = self._manager.application_request(cmd, f"{cmd_base}_list_resp").get(
            field, []
        )
        if not isinstance(res, list):
            res = [res]
        for device_info in res:  # type: DeviceState
            if device_info.get("act_id") == self.act_id:
                self.update_state(device_info)
                return

    @abstractmethod
    def update(self):
        """Update device state."""
        raise NotImplementedError

    @property
    def device_class(self) -> Optional[str]:
        """Return the class of this device."""
        return self._device_class

