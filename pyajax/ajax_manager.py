"""Python client for ETI/Domo."""

import json
import logging
from typing import List, Optional

import requests

from pyajax.const import DEBUG_DEEP, STARTUP_MESSAGE, VERSION
from pyajax.exceptions import (
    AjaxSystemConnectionError,
    AjaxSystemConnectionTimeoutError,
    AjaxSystemError,
)


_LOGGER = logging.getLogger(__name__)

_STARTUP = []


class AjaxManager:
    """Main class for handling connections with an Ajax System device."""

    def __init__(
        self,
        login: str, #Account Mail
        password_hash: str, #Account Password
        user_role: str, #Generally "USER"
        x_api_key: str, #x_api_key provided by Ajax Team
        session: Optional[requests.Session] = None,
    ):
        """Initialize connection with the ETI/Domo."""
        if not _STARTUP:
            _LOGGER.info(STARTUP_MESSAGE)
            _STARTUP.append(True)

        if x_api_key is None or x_api_key == "":
            raise ValueError("A valid X Api Key is REQUIRED.")

        _LOGGER.debug("SetupAjax System API for %s@%s", login, user_role, x_api_key)

        self._login = login
        self._password_hash = password_hash
        self._user_role = user_role
        self._x_api_key = x_api_key
        self._session = session or requests.Session()
        self._session_token = session_token
        self._user_id = _user_id
        self._refresh_token = refresh_token
        self._hub_id = hub_id

        self._features = []


    @property
    def software_version(self) -> Optional[str]:
        """Return a software version of Ajax System."""
        return self._swver



    def _request(self, command: dict, resp_command: str = None) -> dict:
        """Handle a request to an Ajax System device."""
        url = f"https://api.ajax.systems/api/login"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Api_Key": {self._x_api_key},
            "X-Session-Token" : {self._session_token}
        }

        try:
            if DEBUG_DEEP:
                _LOGGER.debug("Send API request: %s", command)

            response = self._session.post(
                url, data={"command": json.dumps(command)}, headers=headers
            )
            response.raise_for_status()

            if DEBUG_DEEP:
                _LOGGER.debug("Response: %s", response.text)

        except requests.exceptions.ConnectTimeout as exception:
            raise AjaxSystemConnectionTimeoutError(
                "Timeout occurred while connecting to Ajax System device."
            ) from exception

        except (
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
            requests.exceptions.BaseHTTPError,
        ) as exception:
            raise AjaxSystemConnectionError(
                "Error occurred while communicating with Ajax System device."
            ) from exception

        try:
            resp_json = response.json()
            errors = resp_json.get("errors")

            if errors == []:#Empty response
                cmd_name = resp_json.get("errors")
                if resp_command is not None and cmd_name != resp_command:
                    raise AjaxSystemError(
                        "Invalid server response. Expected {}. Actual {}".format(
                            repr(resp_command), repr(cmd_name)
                        )
                    )

                return resp_json

            errors = {#DA COMPILARE VERIFICARE CON LE API DI CAME
                1: "Invalid request format or request can't be executed because of some limitations",#400
                2:"	Client is not authorized to perform the operation"#401
                3: "Client doesn't have sufficient permissions to perform the operation",#403
                4: "Requested resource is missing",#404
                5: "Invalid incoming parameters",#422
                6: "Unexpected error happened on the server. The message doesn't contain any details but provides messageId parameter",#500
                7: "The service or one of underlying services can't accept or process incoming request",#503
                8: "The service or one of underlying services failed to respond with some reasonable timeout",#504

            }

            if errors in errors:#error in errors da compilare
                raise AjaxSystemError(errors[errors], errno=errors)

            raise AjaxSystemError(
                f"Unknown error (#{errors}).",
                errno=ack_reason,
            )

        except ValueError as ex:
            raise AjaxSystemError("Error in errors, can't find value.") from ex



            #VEDERE SE "ERRORS" SI PUO' SOSTITUIRE CON "MESSAGE"

#sample di errore
            #{
#  "message": "string",
#  "messageId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
#  "errors": [
#    {
#      "resource": "string",
#      "field": "string",
#      "code": "string",
#      "message": "string"
#    }
#  ]
#}

    @property
    def connected(self) -> bool:
        """Return True if entity is available."""
        return self._session_token is not None

    def login(self) -> None:
        """Login function for access to Ajax System."""
        if self._session_token:
            return

        _LOGGER.debug("Login attempt")
        response = self._request(
            {
                "login": {self._login},
                "passwordHash": {self._password_hash},
                "userRole": {self._user_role},
            },
        )

        try:
            if response["sessionToken"]:
                _LOGGER.debug("Successful authorization.")
                self._session_token = response.get("sessionToken")
                self._user_id = response.get("userId")
                self._refresh_token = response.get("refreshToken")
            else:
                raise AjaxSystemError("Error in sessionToken, can't get value.")
        except KeyError as ex:
            raise AjaxSystemError("Error in sessionToken, can't find value.") from ex

    def application_request(
        self, command: dict, resp_command: str = "generic_reply"
    ) -> dict:
        """Handle a request to application layer to Ajax System."""
        self.login()

        if DEBUG_DEEP:
            _LOGGER.debug("Send application layer API request: %s", command)

        cmd = command.copy()

        try:
            response = self._request(
                {
                    "login": self._login,
                    "passwordHash": self._password_hash,
                    "userRole": self._user_role,
                },
            )
        except AjaxSystemConnectionError as err:
            _LOGGER.debug("Server goes offline.")
            self._user_id = None
            raise err

        if resp_command is not None and response.get("userId") != resp_command:
            raise AjaxSystemError(
                "Invalid server response. Expected {}. Actual {}".format(
                    repr(resp_command), repr(response.get("userId"))
                )
            )

        return response

    def _get_hub_list(self, command: dict, resp_command: str = None) -> dict:
        """Get list of available hubs."""
        url =f"https://api.ajax.systems/api/user/4C6BABCF/hubs"
            return self._hub_id
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "X-Session-Token" : {self._session_token}
            }

#
#
#
#
#
#










# DA DEFINIRE CON UNA RICHIESTA DI DEVICES LIST
#    def get_all_devices(self) -> Optional[List[CameDevice]]:
#        """Get list of all discovered devices."""
#        return self._update_devices()
#
#    def get_device_by_id(self, device_id: str) -> Optional[CameDevice]:
#        """Get device by unique ID."""
#        for device in self.get_all_devices():
#            if device.unique_id == device_id:
#                return device
#
#        return None

#    def get_device_by_act_id(self, act_id: int) -> Optional[CameDevice]:
#        """Get device by device's act ID."""
#        for device in self.get_all_devices():
#            if device.act_id == act_id:
#                return device

#        return None

#    def get_device_by_name(self, name: str) -> Optional[CameDevice]:
#        """Get device by name."""
#        for device in self.get_all_devices():
#            if device.name == name:
#                return device

#        return None



#    def status_update(self, timeout: Optional[int] = None) -> bool:
#        """Long polling method which read status updates."""
#        if self._devices is None:
#            self._update_devices()
#            return True
#
#        cmd = {
#            "cmd_name": "status_update_req",
#        }
#        if timeout is not None:
#            cmd["timeout"] = timeout
#        response = self.application_request(cmd, "status_update_resp")
#
#        updated = False
#
#        for device_info in response.get("result", []):  # type: DeviceState
#            if device_info.get("cmd_name") == "plant_update_ind":
#                self._devices = None
#                self._update_devices()
#                return True
#
#            act_id = device_info.get("act_id")
#            if act_id:
#                device = self.get_device_by_act_id(act_id)
#                if device is not None:
#                    updated |= device.update_state(device_info)
#
#        return updated
