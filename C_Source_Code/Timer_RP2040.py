
# import cog
from common_types import fileMetaData, function, parameter

"""
VERSION CHECK
"""
TIMER_RP2040_TEMPLATE_MAJOR_VERSION = 0x00
TIMER_RP2040_TEMPLATE_MINOR_VERSION = 0x01
TIMER_RP2040_TEMPLATE_BUGFIX_VERSION = 0x00
if fileMetaData.majorVersion != TIMER_RP2040_TEMPLATE_MAJOR_VERSION:
    raise ValueError(" common_types.fileMetaData.majorVersion %s is incompatible with TIMER_RP2040 major version %s" % (fileMetaData.majorVersion, TIMER_RP2040_TEMPLATE_MAJOR_VERSION))
if fileMetaData.minorVersion != TIMER_RP2040_TEMPLATE_MINOR_VERSION:
    raise ValueError(" common_types.fileMetaData.majorVersion %s is incompatible with TIMER_RP2040 major version %s" % (fileMetaData.minorVersion, TIMER_RP2040_TEMPLATE_MINOR_VERSION))


FUNC_PREFIX = "Timer_RP2040_"

STANDARD_RETURN_DESCR_VOID_INIT = \
"\
 * @return \n\
 *         0: 'E_OK' if successful \n\
 *         1: 'E_NOT_OK' if the operation is not successful"

STANDARD_RETURN_DESCR = \
"\
 * @return \n\
 *         0: 'E_OK' if successful \n\
 *         1: 'E_NOT_OK' if the operation is not successful \n\
 *         2: 'E_PARAM' if the input parameter is not valid \n\
 *         3: 'E_MODULE_UNINIT' if the timer is not yet initialized"

STANDARD_RETURN_DESCR_VOID = \
"\
 * @return \n\
 *         0: 'E_OK' if successful \n\
 *         1: 'E_NOT_OK' if the operation is not successful \n\
 *         3: 'E_MODULE_UNINIT' if the timer is not yet initialized"


"""
FILE DATA
"""
fileData = fileMetaData()
fileData.setModuleName("Timer_RP2040")
fileData.setAuthor("Madrick3")
fileData.setBrief("Initializes, manages, and clears timers. Also manages the alarms which may trigger interrupts.")
fileData.includeList.append("Platform_Types.h")
fileData.includeList.append("Timer_RP2040_SFR.h")

"""
Local Functions
"""

#Timer Pause
TIMER_PAUSE = function()
TIMER_PAUSE.setFuncName(FUNC_PREFIX + "Pause")
TIMER_PAUSE.setDescription("Writes to the TIMER_PAUSE register, reports E_OK if Timer is paused. Reports E_NOT_OK if the timer did not pause.")
TIMER_PAUSE.setReturnType("Std_ErrorCode")
TIMER_PAUSE.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
fileData.addPrivateFunctions(TIMER_PAUSE)

#Timer unpause
TIMER_UNPAUSE = function()
TIMER_UNPAUSE.setFuncName(FUNC_PREFIX + "Unpause")
TIMER_UNPAUSE.setDescription("Writes to the TIMER_PAUSE register, reports OK if Timer is unpaused. Reports NOT_OK if the timer did not unpause. There is possible room for improvement here in reporting E_NOT_OK in the case that the timer was not paused already.")
TIMER_UNPAUSE.setReturnType("Std_ErrorCode")
TIMER_UNPAUSE.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
fileData.addPrivateFunctions(TIMER_UNPAUSE)

# Timer_RP2040_ReadTimerLow
TIMER_RP2040_READTIMERLOW = function()
TIMER_RP2040_READTIMERLOW.setFuncName(FUNC_PREFIX + "ReadTimerLow")
TIMER_RP2040_READTIMERLOW.setDescription("Reads from TIMER_TIMELR register. Reports bits {31:0} in the out buffer 'TimerLow'.")
TIMER_RP2040_READTIMERLOW.setReturnType("Std_ErrorCode")
TIMER_RP2040_READTIMERLOW.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_RP2040_READTIMERLOW_P_TIMERLOW = parameter()
TIMER_RP2040_READTIMERLOW_P_TIMERLOW.setBrief("Output buffer for TIMEL read")
TIMER_RP2040_READTIMERLOW_P_TIMERLOW.setName("TimerLow")
TIMER_RP2040_READTIMERLOW_P_TIMERLOW.setType(" uint32 * ")
TIMER_RP2040_READTIMERLOW.addParameter(TIMER_RP2040_READTIMERLOW_P_TIMERLOW)
fileData.addPrivateFunctions(TIMER_RP2040_READTIMERLOW)

# Timer_RP2040_ReadTimerHigh
TIMER_RP2040_READTIMERHIGH = function()
TIMER_RP2040_READTIMERHIGH.setFuncName(FUNC_PREFIX + "ReadTimerHigh")
TIMER_RP2040_READTIMERHIGH.setDescription("Reads from TIMER_TIMEHR register. Reports bits {63:32} in the out buffer 'TimerHigh'.")
TIMER_RP2040_READTIMERHIGH.setReturnType("Std_ErrorCode")
TIMER_RP2040_READTIMERHIGH.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_RP2040_READTIMERHIGH_P_TIMERHIGH = parameter()
TIMER_RP2040_READTIMERHIGH_P_TIMERHIGH.setBrief("Output buffer for TIMEH read")
TIMER_RP2040_READTIMERHIGH_P_TIMERHIGH.setName("TimerHigh")
TIMER_RP2040_READTIMERHIGH_P_TIMERHIGH.setType(" uint32 * ")
TIMER_RP2040_READTIMERHIGH.addParameter(TIMER_RP2040_READTIMERHIGH_P_TIMERHIGH)
fileData.addPrivateFunctions(TIMER_RP2040_READTIMERHIGH)

# Timer_RP2040_WriteTimerLow
TIMER_RP2040_WRITETIMERLOW = function()
TIMER_RP2040_WRITETIMERLOW.setFuncName(FUNC_PREFIX + "WriteTimerLow")
TIMER_RP2040_WRITETIMERLOW.setDescription("Writes to TIMER_TIMELW register. Does not perform input checking")
TIMER_RP2040_WRITETIMERLOW.setReturnType("Std_ErrorCode")
TIMER_RP2040_WRITETIMERLOW.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
TIMER_RP2040_WRITETIMERLOW_P_TIMERLOW = parameter()
TIMER_RP2040_WRITETIMERLOW_P_TIMERLOW.setBrief("Input word for TIMEL write")
TIMER_RP2040_WRITETIMERLOW_P_TIMERLOW.setName("TimerLow")
TIMER_RP2040_WRITETIMERLOW_P_TIMERLOW.setType(" uint32 ")
TIMER_RP2040_WRITETIMERLOW.addParameter(TIMER_RP2040_WRITETIMERLOW_P_TIMERLOW)
fileData.addPrivateFunctions(TIMER_RP2040_WRITETIMERLOW)

# Timer_RP2040_WriteTimerHigh
TIMER_RP2040_WRITETIMERHIGH = function()
TIMER_RP2040_WRITETIMERHIGH.setFuncName(FUNC_PREFIX + "WriteTimerHigh")
TIMER_RP2040_WRITETIMERHIGH.setDescription("Writes to TIMER_TIMEHW register. Does not perform input checking.")
TIMER_RP2040_WRITETIMERHIGH.setReturnType("Std_ErrorCode")
TIMER_RP2040_WRITETIMERHIGH.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
TIMER_RP2040_WRITETIMERHIGH_P_TIMERHIGH = parameter()
TIMER_RP2040_WRITETIMERHIGH_P_TIMERHIGH.setBrief("Input word for TIMEH read")
TIMER_RP2040_WRITETIMERHIGH_P_TIMERHIGH.setName("TimerHigh")
TIMER_RP2040_WRITETIMERHIGH_P_TIMERHIGH.setType(" uint32 ")
TIMER_RP2040_WRITETIMERHIGH.addParameter(TIMER_RP2040_WRITETIMERHIGH_P_TIMERHIGH)
fileData.addPrivateFunctions(TIMER_RP2040_WRITETIMERHIGH)

"""
Public Functions
"""

#Timer Init
TIMER_INIT = function()
TIMER_INIT.setFuncName(FUNC_PREFIX + "Init")
TIMER_INIT.setDescription("Initializes the timer module for a basic runtime implemetations: Arms ALARM0 as a 1ms timer, clears TIME, and begins the timer. Can fail if the RP2040_Watchdog is not already initialized. (See RP2040 datasheet section 4.7.2 'Tick Generation'). Interrupts are not necessarily enabled at this stage.")
TIMER_INIT.setBrief("Initializes the RP2040  timer. Prepares ALARM0 for 1ms triggeers. Will fail if the tick generation is not yet initialized.")
TIMER_INIT.setReturnType("Std_ErrorCode")
TIMER_INIT.setReturnDesc(STANDARD_RETURN_DESCR_VOID_INIT)
TIMER_INIT.setPreCondition(" Tick generation is already started in the watchdog module. ")
TIMER_INIT.setPostCondition(" ALARM0 is armed. ")
fileData.addPublicFunctions(TIMER_INIT)

#Timer DeInit
TIMER_DEINIT = function()
TIMER_DEINIT.setFuncName(FUNC_PREFIX + "Deinit")
TIMER_DEINIT.setDescription("Updates internal tracking variables that the timer is 'uninit'. Disables all alarms. Pauses the timer. Expects that the timer module was previously enabled, and will report an error if the module was not initialized.\
 Will disable interrupts as well.")
TIMER_DEINIT.setBrief("Deinitializes the timer software module. Disables all alarms, Pauses the timer register, but does not reset the timer.")
TIMER_DEINIT.setReturnType("Std_ErrorCode")
TIMER_DEINIT.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
TIMER_DEINIT.setPreCondition("Timer module was previously enabled.")
TIMER_DEINIT.setPostCondition("Alarms are all disabeled, Timer is paused.")
fileData.addPublicFunctions(TIMER_DEINIT)

#Timer Interrupt Enable
# TIMER_DEINIT = function()
# TIMER_DEINIT.setFuncName(FUNC_PREFIX + "InterruptEnable")
# TIMER_DEINIT.setDescription("")
# TIMER_DEINIT.setBrief("Deinitializes the timer software module. Disables all alarms, Pauses the timer register, but does not reset the timer.")
# TIMER_DEINIT.setReturnType("Std_ErrorCode")
# TIMER_DEINIT.setReturnDesc(STANDARD_RETURN_DESCR_VOID)
# TIMER_DEINIT.setPreCondition("Timer module was previously enabled.")
# TIMER_DEINIT.setPostCondition("Alarms are all disabeled, Timer is paused.")
# fileData.addPublicFunctions(TIMER_DEINIT)
