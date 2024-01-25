#features to develop: ARM, DISARM, ARM_NIGHT, 
#STATUS (ARMED, DISARMED, ARMED_NIGHT)
#SENSORS WIFI AND SIM CARD SIGNAL



#API DATA

Hub2Plus{
id	string($hex64)
readOnly: true
name*	string
minLength: 1
maxLength: 24
Name length may depend on language and how many bytes needed to encode single character

panicSirenOnPanicButton*	boolean
state	string
readOnly: true
If group mode is disabled then possible values are: DISARMED, ARMED, NIGHT_MODE. Otherwise one of the remaining values will be returned.

Enum:
[ DISARMED, ARMED, NIGHT_MODE, ARMED_NIGHT_MODE_ON, ARMED_NIGHT_MODE_OFF, DISARMED_NIGHT_MODE_ON, DISARMED_NIGHT_MODE_OFF, PARTIALLY_ARMED_NIGHT_MODE_ON, PARTIALLY_ARMED_NIGHT_MODE_OFF ]
limits	HubLimits{
rooms	integer($int32)
readOnly: true
groups	integer($int32)
readOnly: true
cameras	integer($int32)
readOnly: true
sensors	integer($int32)
readOnly: true
users	integer($int32)
readOnly: true
}
groupsEnabled	boolean
readOnly: true
firmware*	HubFirmware{
version	string
readOnly: true
newVersionAvailable	boolean
readOnly: true
latestAvailableVersion	string
readOnly: true
autoupdateEnabled*	boolean
}
ethernet	HubEthernet{
enabled	boolean
readOnly: true
dns	string($ipv4)
readOnly: true
ip	string($ipv4)
readOnly: true
gate	string($ipv4)
readOnly: true
dhcp	boolean
readOnly: true
mask	string($ipv4)
readOnly: true
}
armPreventionMode*	string
Enum:
[ IGNORE_WARNINGS, ALERT_USER, PREVENT_ARMING ]
tampered	boolean
readOnly: true
panicSirenOnAnyTamper*	boolean
battery	HubBattery{
chargeLevelPercentage	integer($int32)
readOnly: true
state	string
readOnly: true
Enum:
[ CHARGED, DISCHARGED, MALFUNCTION ]
}
hardwareVersions	HubHardwareVersions{
cpu	integer
readOnly: true
wifi	integer
readOnly: true
ethernet	integer
readOnly: true
flash	integer
readOnly: true
pcb	integer
readOnly: true
rfm	integer
readOnly: true
zwave	integer
readOnly: true
modem	integer
readOnly: true
}
warnings	HubWarnings{
hub	integer($int32)
readOnly: true
allDevices	integer($int32)
readOnly: true
}
fireAlarm*	HubFireAlarm{
triggerOnAllSensors*	boolean
Enables alarm propagation to all all fire protect devices. May not be set to true if hub.jeweller.detectorPingIntervalSeconds is greater than 48.

doubleImpulses*	boolean
alarmPropagationTimeoutSeconds	integer($int32)
minimum: 0
maximum: 300
multipleOf: 60
alarmPropagationTimeoutExpirationTimestamp	integer($int32)
readOnly: true
alarmPropagationState	string
readOnly: true
Enum:
[ DISABLED, DELAYED, MUTED_BY_USER, IN_PROGRESS ]
alarmPropagationDetails	{
multiApartmentBuildingModeEnabled*	[...]
}
}
color	string
readOnly: true
Enum:
[ WHITE, BLACK ]
imageUrls	ImageUrls{
small	string
readOnly: true
medium	string
readOnly: true
big	string
readOnly: true
}
activeChannels	[
readOnly: true
HubNetworkChannelstring
Enum:
[ GSM, WIFI, ETHERNET ]
]
pingPeriodSeconds*	integer($int32)
minimum: 10
maximum: 300
offlineAlarmSeconds*	integer($int32)
minimum: 30
maximum: 600
ledBrightnessLevel*	integer($int32)
minimum: 0
maximum: 10
jeweller*	HubJeweller{
lostHeartbeatsThreshold*	integer($int32)
minimum: 3
maximum: 60
Number or undelivered packets to determine connection failure

detectorPingIntervalSeconds*	integer($int32)
minimum: 12
maximum: 300
Detector ping interval. Should be multiple of 12. May not be greater than 48 if hub.fireAlarm.triggerOnAllSensors is set to true.

}
externallyPowered	boolean
readOnly: true
connectionTestInProgress	boolean
readOnly: true
blockedByServiceProvider	boolean
readOnly: true
connectionLostAsMalfunction*	boolean
alarmAsMalfunctionWhenArming*	boolean
hubAddress	HubAddress{
countryCode	string
maxLength: 2
ISO 3166-1 alpha-2 country code according to https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes, empty country code is mapped to null for backwards-compatibility

locState	string
maxLength: 50
State, region or province.

locality	string
maxLength: 50
City, town or village.

address	string
maxLength: 500
Street.

comment	string
maxLength: 500
Additional data.

latitude	string
minLength: 1
Latitude with maximum precision of 6 digits after decimal point, minimum -90, maximum 90.

longitude	string
minLength: 1
Longitude with maximum precision of 6 digits after decimal point, minimum -180, maximum 180.

}
alarmVerification	AlarmVerification{
verificationEnabled	boolean
Deprecated, use alarmConfirmation instead. If true, hub will send alarm verification to security company. Nullable.

verificationTimeout	integer($int32)
minimum: 30
maximum: 60
multipleOf: 5
Deprecated, use alarmConfirmation instead. Alarm verification timeout for hold up devices (minutes).

}
alarmConfirmation	AlarmConfirmation{
commonDevice	CommonDeviceAlarmConfirmation{
status	string
default: DISABLED
If ENABLED, hub will send alarm confirmation to security company

Enum:
[ ENABLED, DISABLED ]
timeoutMinutes	integer($int32)
minimum: 30
maximum: 60
multipleOf: 5
Alarm validation timeout for devices (minutes)

confirmedAlarmOn	[string
Enum:
[ TAMPER, DELAYED_DEVICES ]
]
}
holdUpDevice	HoldUpDeviceAlarmConfirmation{
status	string
default: DISABLED
If ENABLED, hub will send hold up devices alarm confirmation to security company

Enum:
[ ENABLED, DISABLED ]
timeoutMinutes	integer
minimum: 480
maximum: 1200
multipleOf: 60
Alarm validation timeout for hold up devices (minutes)

}
}
geoFence	GeoFence{...}
hubMalfunctions	[...]
timeZone	[...]
armPreventionConditions	[...]
restoreRequiredAfterAlarmCondition	[...]
alarmCondition	[...]
twoStageArming	HubTwoStageArming{
enabled*	boolean
applicationTriggeredArming*	HubApplicationTriggeredArming{
countdownDurationSeconds*	integer($int32)
minimum: 30
maximum: 60
state	string
readOnly: true
Enum:
[ NOT_STARTED, IN_PROGRESS ]
expirationUnixTime	integer($int32)
readOnly: true
}
deviceTriggeredArming*	HubDeviceTriggeredArming{
countdownDurationSeconds*	integer($int32)
minimum: 60
maximum: 240
finalDoorBounceCountdownDurationSeconds*	integer($int32)
minimum: 0
maximum: 5
state	string
readOnly: true
Enum:
[ NOT_STARTED, MAIN_COUNTDOWN_IN_PROGRESS, FINAL_DOOR_BOUNCE_COUNTDOWN_IN_PROGRESS, INCOMPLETE ]
expirationUnixTime	integer($int32)
readOnly: true
}
}
photoOnDemandDetails	PhotoOnDemandDetails{
enabledOnDemandPhotoFeatures	[
readOnly: true
OnDemandPhotoFeaturestring
Enum:
[ MAKE_PHOTO_COMMAND, MAKE_PHOTO_SCENARIO_ACTION ]
]
}
postAlarmIndication	PostAlarmIndication{
enabledIndicationRules*	[PostAlarmIndicationRulestring
Enum:
[ INDICATE_CONFIRMED_ALARMS, INDICATE_UNCONFIRMED_ALARMS, INDICATE_TAMPER_ACTIVATION ]
]
}
ledIndicationMode	LedIndicationModestring
Enum:
[ HUB_SERVER_CONNECTION, ALERTS_AND_MALFUNCTIONS ]
currentStandard	string
Enum:
[ EU, PD, SIACP ]
siaCpSettings	SiaCpStandardSettings{
exitTimeRestart*	boolean
recentClosing*	boolean
alarmCancelWindow*	boolean
unvacatedPremises*	boolean
lastSecondsNotification*	integer
minimum: 5
maximum: 15
}
batterySavingMode	BatterySavingMode{
batterySaveModeEnable*	string
Enum:
[ ENABLED, DISABLED ]
batterySaveModeEnableV2	string
Enum:
[ DISABLED, ENABLED_FOR_INTERNAL_BATTERY, ENABLED_FOR_EXTERNAL_POWER_SOURCE, ENABLED_FOR_ALL_POWER_SOURCES ]
batterySaveModeStatus	string
readOnly: true
Enum:
[ NORMAL, BATTERY_SAVING, UNSPECIFIED ]
batterySaveModeActiveTime*	integer($int32)
minimum: 5
maximum: 60
multipleOf: 5
batterySaveModePingPeriodMin*	integer($int32)
minimum: 60
maximum: 1440
multipleOf: 60
}
eventDelayEnable	[string
Enum:
[ FIRE_PROTECT2_LOST_EXTERNAL_POWER_EVENT ]
]
interconnectWithoutHub	InterconnectWithoutHub{
iwhNetworkTestState	string
readOnly: true
Enum:
Array [ 4 ]
iwhNetworkTestEndTime	integer($int32)
readOnly: true
iwhNetworkTestInitiatorId	string
readOnly: true
iwhEnabled*	string
Enum:
Array [ 2 ]
activeFireAlarms	[
readOnly: true
[...]]
}
modemImei	string
readOnly: true
passwordLength	integer($int32)
readOnly: true
noiseLevel	Hub2PlusNoiseLevel{
high	boolean
readOnly: true
avgValueChannel1	integer($int32)
readOnly: true
avgValueChannel2	integer($int32)
readOnly: true
avgValueDataChannel	integer($int32)
readOnly: true
}
gsm	Hub2PlusGsm{
disableIcmpBeforeConnecting	boolean
readOnly: true
gprsEnabled	boolean
readOnly: true
virtualOperatorAllowed	boolean
readOnly: true
roamingEnabled	boolean
readOnly: true
simCardState	string
readOnly: true
Enum:
[ OK, MISSING, MALFUNCTION, LOCKED, UNKNOWN ]
signalLevel	string
readOnly: true
Enum:
[ NO_SIGNAL, WEAK, NORMAL, STRONG ]
activeSimCard	integer($int32)
readOnly: true
simCards	HubGsmSimCards[HubGsmSimCard{
number	string
readOnly: true
apn	string
readOnly: true
username	string
readOnly: true
password	string
readOnly: true
balanceNumber	string
readOnly: true
trafficTxKb	integer
readOnly: true
trafficRxKb	integer
readOnly: true
lastTrafficResetTimestamp	integer
readOnly: true
linux epoch timestamp when gsm network rx/tx counters were dropped

}]
networkStatus	string
readOnly: true
Enum:
[ UNKNOWN, GSM, 2G, 3G, 4G ]
}
cms*	Hub2PlusCms{
address*	string($ipv4)
Address is used for connecting to primary CMS using Ethernet when cmsProtocol is equal to SIA. Address is used for connecting to primary CMS using all adapters when cmsProtocol is equal to CID

port*	integer($int32)
Port is used for connecting to primary CMS using Ethernet when cmsProtocol is equal to SIA. Port is used for connecting to primary CMS using all adapters when cmsProtocol is equal to CID

addressReserve*	string($ipv4)
Address is used for connecting to secondary CMS using Ethernet when cmsProtocol is equal to SIA. Address is used for connecting to secondary CMS using all adapters when cmsProtocol is equal to CID

portReserve*	integer($int32)
Port is used for connecting to secondary CMS using Ethernet when cmsProtocol is equal to SIA. Port is used for connecting to secondary CMS using all adapters when cmsProtocol is equal to CID

cmsProtocol*	string
Enum:
Array [ 2 ]
cmsConnectionMode*	string
Enum:
Array [ 2 ]
siaAccountNumber*	string
minLength: 0
maxLength: 16
Value must be empty string or a valid hex integer

pingPeriodSeconds*	integer($int32)
minimum: 0
maximum: 86400
Value must be a multiple of 60

gprsEnabled*	boolean
ethernetEnabled*	boolean
siaEncryptionKey	string($password)
minLength: 16
maxLength: 16
AES-128 encryption key. Write only, nullable field.

siaEncryptionType*	string
Enum:
Array [ 3 ]
sendPanicButtonLocation	boolean
Provides location of panic button when triggered. Nullable.

alarmRecoveryNotificationSettings	{
alarmRecoveryReportMode	[...]
additionalAlarmRecoveriesToReport	[...]
}
gprsAddress	string($ipv4)
Address is used for connecting to primary CMS using SIM card when cmsProtocol is equal to SIA

gprsPort	integer($int32)
Port is used for connecting to primary CMS using SIM card when cmsProtocol is equal to SIA

gprsAddressReserve	string($ipv4)
Address is used for connecting to secondary CMS using SIM card when cmsProtocol is equal to SIA

gprsPortReserve	integer($int32)
Port is used for connecting to secondary CMS using SIM card when cmsProtocol is equal to SIA

activeChannels	[
readOnly: true
HubNetworkChannel[...]]
wifiEnabled*	boolean
wifiAddress	string($ipv4)
Address is used for connecting to primary CMS using Wi-Fi when cmsProtocol is equal to SIA

wifiPort	integer($int32)
Port is used for connecting to primary CMS using Wi-Fi when cmsProtocol is equal to SIA

wifiAddressReserve	string($ipv4)
Address is used for connecting to secondary CMS using Wi-Fi when cmsProtocol is equal to SIA

wifiPortReserve	integer($int32)
Port is used for connecting to secondary CMS using Wi-Fi when cmsProtocol is equal to SIA

}
wifi	HubWifi{
enabled	boolean
readOnly: true
ssid	string
readOnly: true
password	string
readOnly: true
channel	integer
readOnly: true
ip	string($ipv4)
readOnly: true
securityProtocol	string
readOnly: true
Enum:
[ NONE, WEP, WPA, WPA2 ]
dhcp	boolean
readOnly: true
gate	string($ipv4)
readOnly: true
dns	string($ipv4)
readOnly: true
signalLevel	string
readOnly: true
Enum:
Array [ 4 ]
mask	string($ipv4)
readOnly: true
}
hubSubtype*	string
Enum:
[ HUB_2_PLUS ]
debugLogState*	string
Enum:
[ NO_LOGS, ETHERNET_ONLY, WIFI_ONLY, ETHERNET_OR_WIFI ]
connectivityNotificationSettings	Hub2PlusConnectivityNotificationSettings{
channelOfflineAlarmDelaySeconds*	integer($int32)
minimum: 180
maximum: 1800
multipleOf: 60
enabledChannelNotifications*	[HubNetworkChannelstring
Enum:
[ GSM, WIFI, ETHERNET ]
]
}
}
