# FEATURES TO DEVELOP: MOTION STATUS, TEMPERATURE SENSOR 


#API_DATA
MotionProtect{
indicatorLightMode	IndicatorLightMode[...]
indicatorLightModeSupported	boolean
readOnly: true
Indicates whether device firmware supports the indicatorLightMode setting. If false, only STANDARD mode is allowed. Hub firmware of version >=2.8.103 is also required for settings to have any effect, otherwise device will behave as if light indicator mode STANDARD was selected.

alwaysActive*	boolean
sensitivity*	integer($int32)
minimum: 0
maximum: 2
sirenTriggers*	[string
Enum:
[ MOTION ]
]
deviceType*	string
Enum:
[ MotionProtect ]
}
