# used for fire protect, water sensors, temperature sensors, etc etc



"""Ajax System analog sensor device."""

import logging
from typing import Optional

from .base import TYPE_ANALOG_SENSOR, AjaxDevice, DeviceState, StateType

_LOGGER = logging.getLogger(__name__)


class AjaxAnalogSensor(AjaxDevice):
    """Ajax System analog sensor device class."""

    def __init__(
        self,
        manager,
        device_info: DeviceState,
        update_cmd_base: str = "thermo",
        update_src_field: str = "array",
        device_class: Optional[str] = None,
    ):
        """Init instance."""
        super().__init__(
            manager, TYPE_ANALOG_SENSOR, device_info, device_class=device_class
        )

        self._update_cmd_base = update_cmd_base
        self._update_src_field = update_src_field

    def update(self):
        """Update device state."""
        self._force_update(self._update_cmd_base, self._update_src_field)

    @property
    def state(self) -> StateType:
        """Return the current device state."""
        return self._device_info.get("value")

    @property
    def unit_of_measurement(self) -> Optional[str]:
        """Return the unit of measurement of this sensor, if any."""
        return self._device_info.get("unit")
