# FEATURES TO DEVELOP: REED STATUS, TEMPERATURE SENSOR EXTERNAL CONTACT (OPTIONAL)



#API DATA

DoorProtect{
id	string
readOnly: true
deviceName*	string
roomId*	string
groupId	string
Must be either existing group id or null (only valid in case groupsMode is turned OFF).

malfunctions	[
readOnly: true
string
Enum:
Array [ 18 ]
]
color	string
readOnly: true
Enum:
[ WHITE, BLACK, RED, BLUE, YELLOW, GREEN ]
temperature	integer($int32)
readOnly: true
signalLevel	string
readOnly: true
Enum:
[ NO_SIGNAL, WEAK, NORMAL, STRONG ]
tampered	boolean
readOnly: true
batteryChargeLevelPercentage	integer($int32)
readOnly: true
firmwareVersion	string
readOnly: true
online	boolean
readOnly: true
issuesCount	integer($int32)
readOnly: true
assignedExtender*	integer($int32)
cmsDeviceIndex	integer($int32)
readOnly: true
deviceTransmissionPowerMode	integer($int32)
minimum: 0
maximum: 3
Deprecated: deviceTransmissionPowerModeValue should be used instead.

deviceTransmissionPowerModeValue	string
Enum:
[ DEFAULT, REDUCED, MAXIMUM ]
nightModeArm*	boolean
imageId	integer($int32)
This field is deprecated and won't be set anymore. Value always will be 0

verifiesAlarm	boolean
Deprecated. Use confirmsAlarm instead. Nullable.

confirmsAlarm	string
Optional field. May be passed, only if Alarm Confirmation is enabled and hub's firmware supports it. If ENABLED, the device would take a part in the alarm confirmation.

Enum:
[ ENABLED, DISABLED ]
armDelaySeconds*	integer($int32)
minimum: 0
maximum: 120
alarmDelaySeconds*	integer($int32)
minimum: 0
maximum: 120
applyDelaysToNightMode	boolean
Applicable for hubs with Firmware version < 2.12.0

state	string
readOnly: true
Enum:
[ PASSIVE, ACTIVE, DETECTION_AREA_TEST, RADIO_CONNECTION_TEST, WAIT_RADIO_CONNECTION_TEST_START, WAIT_RADIO_CONNECTION_TEST_END, WAIT_DETECTION_AREA_TEST_START, WAIT_DETECTION_AREA_TEST_END, WAIT_REGISTRATION, WAIT_RADIO_CHANNEL_TEST_START, RADIO_CHANNEL_TEST, WAIT_RADIO_CHANNEL_TEST_END, CALIBRATION_IN_PROGRESS, MAXIMUM_BUS_POWER_CONSUMPTION_TEST_IN_PROGRESS, DEVICE_IS_IN_FILE_RECEIVING_MODE_WINGS, DEVICE_IS_INSTALLING_FIRMWARE, SELF_TEST_IN_PROGRESS ]
bypassState	[
readOnly: true
string
Enum:
[ ENGINEER_BYPASS_ACTIVE, TAMPER_BYPASS_ACTIVE, AUTO_BYPASSED_BY_ALARMS_COUNT, AUTO_BYPASSED_AS_NOT_RESTORED, ONETIME_FULL_BYPASS_ENABLED, ONETIME_TAMPER_BYPASS_ENABLED ]
]
estimatedArmingState	string
readOnly: true
Enum:
[ DISARMED, ARMED ]
armDelaySecondsInNightMode	integer($int32)
minimum: 0
maximum: 120
alarmDelaySecondsInNightMode	integer($int32)
minimum: 0
maximum: 120
selfMonitoringConfig	string
Enum:
[ LOCAL_ALARM_DISABLED, LOCAL_ALARM_ENABLED ]
armingMode	string
Enum:
[ NORMAL, ENTRY_EXIT, FOLLOWER ]
indicatorLightMode	IndicatorLightModestring
Enum:
[ STANDARD, DONT_BLINK_ON_ALARM ]
indicatorLightModeSupported	boolean
readOnly: true
Indicates whether device firmware supports the indicatorLightMode setting. If false, only STANDARD mode is allowed. Hub firmware of version >=2.8.103 is also required for settings to have any effect, otherwise device will behave as if light indicator mode STANDARD was selected.

alwaysActive*	boolean
extraContactAware*	boolean
reedContactAware*	boolean
reedClosed	boolean
readOnly: true
extraContactClosed	boolean
readOnly: true
sirenTriggers*	[string
Enum:
Array [ 2 ]
]
twoStageArmingRole	{
description:	
Optional field. If set to ARMING_COMPLETION_DEVICE, device alarm will trigger completion of the second stage of device-triggered two stage arming. DoorProtect must have either extraContactAware or reedContactAware set to true in order for it to act as an ARMING_COMPLETION_DEVICE. May be passed, only if TwoStageArming is enabled and hub's firmware supports it.

}
deviceType*	string
Enum:
[ DoorProtect ]
}
