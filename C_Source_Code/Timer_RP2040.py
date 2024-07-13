
# import cog
from common_types import fileMetaData, function, parameter

"""
VERSION CHECK
"""
TIMER_RP2040_TEMPLATE_MAJOR_VERSION = "00"
TIMER_RP2040_TEMPLATE_MINOR_VERSION = "01"
TIMER_RP2040_TEMPLATE_BUGFIX_VERSION = "00"
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
fileData.setBrief("Provides a global timebase for software through the generation of a global microsecond timebase. The timebase relies on a  one microsend reference that is generated in the watchdog, and is derived from the reference clock (REFCLK). A 64-bit timer is managed, and is not able to overflow on it's own - thoughtful use of the module provides completely monotic use in practice, although setting the time to a specific large value like 0xFFFFFFFF will result in overflow. Otherwise, the module initializes, manages, and clears the timer, also manages the alarms which may trigger interrupts.")
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
TIMER_INTENABLE = function()
TIMER_INTENABLE.setFuncName(FUNC_PREFIX + "InterruptEnable")
TIMER_INTENABLE.setDescription("Writes directly to the TIMER_INTE register, given an uint8 bitmask. Will report a parameter failure if the bitmask parameter is not within the acceptable range [1,15]. Will not disable, clear, or otherwise touch alarms.")
TIMER_INTENABLE.setBrief("Enables interrupts for the ALARMS given by the bitmask parameter.")
TIMER_INTENABLE.setReturnType("Std_ErrorCode")
TIMER_INTENABLE.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_INTENABLE.setPreCondition("Timer module was previously enabled.")
TIMER_INTENABLE.setPostCondition("Interrupts are enabled.")
TIMER_INTENABLE_BITMASK = parameter()
TIMER_INTENABLE_BITMASK.setBrief("Bitmask for which interrupts should be enabled. Acceptable values are between (and including) 1d (0b0001) and 15d (0b1111)")
TIMER_INTENABLE_BITMASK.setName("int_bitmask")
TIMER_INTENABLE_BITMASK.setType(" uint8 ")
TIMER_INTENABLE.addParameter(TIMER_INTENABLE_BITMASK)
fileData.addPublicFunctions(TIMER_INTENABLE)

#Timer Interrupt Disable
TIMER_INTDISABLE = function()
TIMER_INTDISABLE.setFuncName(FUNC_PREFIX + "InterruptDisable")
TIMER_INTDISABLE.setDescription("Writes directly to the TIMER_INTE register, given an uint8 bitmask. Will report a parameter failure if the bitmask parameter is not within the acceptable range [1,15]. Will not disable, clear, or otherwise touch alarms.")
TIMER_INTDISABLE.setBrief("Disables interrupts for the ALARMS given by the bitmask parameter.")
TIMER_INTDISABLE.setReturnType("Std_ErrorCode")
TIMER_INTDISABLE.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_INTDISABLE.setPreCondition("Timer module was previously enabled.")
TIMER_INTDISABLE.setPostCondition("Interrupts are disabled.")
TIMER_INTDISABLE_BITMASK = parameter()
TIMER_INTDISABLE_BITMASK.setBrief("Bitmask for which interrupts should be disabled. Acceptable values are between (and including) 1d (0b0001) and 15d (0b1111)")
TIMER_INTDISABLE_BITMASK.setName("int_bitmask")
TIMER_INTDISABLE_BITMASK.setType(" uint8 ")
TIMER_INTDISABLE.addParameter(TIMER_INTDISABLE_BITMASK)
fileData.addPublicFunctions(TIMER_INTDISABLE)

#Timer Interrupt Trigger
# Something to consider adding in the future, but the handling of the interrupts in the function could cause problems. Want to avoid this for now.
# TIMER_INTENABLE = function()
# TIMER_INTENABLE.setFuncName(FUNC_PREFIX + "InterruptTrigger")
# TIMER_INTENABLE.setDescription("Writes directly to the TIMER_INTF register, given an uint8 bitmask. Will report a parameter failure if the bitmask parameter is not within the acceptable range [1,15]. Can be used for testing purposes, or to enforce handling sooner than ALARM")
# TIMER_INTENABLE.setBrief("Sets interrupt flags for the ALARMS given by the bitmask parameter.")
# TIMER_INTENABLE.setReturnType("Std_ErrorCode")
# TIMER_INTENABLE.setReturnDesc(STANDARD_RETURN_DESCR)
# TIMER_INTENABLE.setPreCondition("Timer module was previously enabled.")
# TIMER_INTENABLE.setPostCondition("Interrupts were tr.")
# TIMER_INTENABLE_BITMASK = parameter()
# TIMER_INTENABLE_BITMASK.setBrief("Bitmask for which interrupts should be enabled. Acceptable values are between (and including) 1d (0b0001) and 15d (0b1111)")
# TIMER_INTENABLE_BITMASK.setName("int_bitmask")
# TIMER_INTENABLE_BITMASK.setType(" uint8 ")
# TIMER_INTENABLE.addParameter(TIMER_INTENABLE_BITMASK)
# fileData.addPublicFunctions(TIMER_INTENABLE)

TIMER_READTIMER = function()
TIMER_READTIMER.setFuncName(FUNC_PREFIX + "TimerRead")
TIMER_READTIMER.setDescription("Reads from TIMER_TIMELR and TIMER_TIMEHR. Is not threadsafe - future improvements can be made by utilizing the RAWL and RAWH registers instead. This read is not threadsafe, and enforces latching on the timer, so interrupts should be stopped specifically during this read.")
TIMER_READTIMER.setBrief("Reads 64 bit timer and reports the data back in two 32 bit values (high and low)")
TIMER_READTIMER.setReturnType("Std_ErrorCode")
TIMER_READTIMER.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_READTIMER.setPreCondition("n/a")
TIMER_READTIMER.setPostCondition("n/a")
TIMER_READTIMER_TIMERHIGH = parameter()
TIMER_READTIMER_TIMERHIGH.setBrief("Pointer to where timer bits [63:32] will be stored.")
TIMER_READTIMER_TIMERHIGH.setName("TimerHigh")
TIMER_READTIMER_TIMERHIGH.setType(" uint32 * ")
TIMER_READTIMER.addParameter(TIMER_READTIMER_TIMERHIGH)
TIMER_READTIMER_TIMERLOW = parameter()
TIMER_READTIMER_TIMERLOW.setBrief("Pointer to where timer bits [31:0] will be stored.")
TIMER_READTIMER_TIMERLOW.setName("TimerLow")
TIMER_READTIMER_TIMERLOW.setType(" uint32 * ")
TIMER_READTIMER.addParameter(TIMER_READTIMER_TIMERLOW)
fileData.addPublicFunctions(TIMER_READTIMER)

TIMER_WRITETIMER = function()
TIMER_WRITETIMER.setFuncName(FUNC_PREFIX + "TimerWrite")
TIMER_WRITETIMER.setDescription("Writes to TIMER_TIMELW and TIMER_TIMEHW. Is not threadsafe - future improvements can be made by utilizing the RAWL and RAWH registers instead. This write is not threadsafe, and enforces latching on the timer, so interrupts should be stopped specifically during this write.")
TIMER_WRITETIMER.setBrief("Writes 64 bit timer values to the timer utilizing two 32 bit integers.")
TIMER_WRITETIMER.setReturnType("Std_ErrorCode")
TIMER_WRITETIMER.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_WRITETIMER.setPreCondition("n/a")
TIMER_WRITETIMER.setPostCondition("n/a")
TIMER_WRITETIMER_TIMERHIGH = parameter()
TIMER_WRITETIMER_TIMERHIGH.setBrief("Pointer to where timer bits [63:32] will be loaded from.")
TIMER_WRITETIMER_TIMERHIGH.setName("TimerHigh")
TIMER_WRITETIMER_TIMERHIGH.setType(" uint32 * ")
TIMER_WRITETIMER.addParameter(TIMER_WRITETIMER_TIMERHIGH)
TIMER_WRITETIMER_TIMERLOW = parameter()
TIMER_WRITETIMER_TIMERLOW.setBrief("Pointer to where timer bits [31:0] will be loaded from.")
TIMER_WRITETIMER_TIMERLOW.setName("TimerLow")
TIMER_WRITETIMER_TIMERLOW.setType(" uint32 * ")
TIMER_WRITETIMER.addParameter(TIMER_WRITETIMER_TIMERLOW)
fileData.addPublicFunctions(TIMER_WRITETIMER)

# Std_ReturnType Timer_RP2040_ReadTimer_32 ( uint32 * TimerLow );
TIMER_READTIMER32 = function()
TIMER_READTIMER32.setFuncName(FUNC_PREFIX + "TimerRead32")
TIMER_READTIMER32.setDescription("Reads from TimerAWL. Stores the result in the input buffer provided. Does not lock or cause any side-effects.")
TIMER_READTIMER32.setBrief("Reads the timer from TIMER_TIMERAWL - stores the result in the buffer provided.")
TIMER_READTIMER32.setReturnType("Std_ErrorCode")
TIMER_READTIMER32.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_READTIMER32.setPreCondition("n/a")
TIMER_READTIMER32.setPostCondition("n/a")
TIMER_READTIMER32_TIMERLOW = parameter()
TIMER_READTIMER32_TIMERLOW.setBrief("Pointer to where timer bits [31:0] will be stored.")
TIMER_READTIMER32_TIMERLOW.setName("TimerLow")
TIMER_READTIMER32_TIMERLOW.setType(" uint32 * ")
TIMER_READTIMER32.addParameter(TIMER_READTIMER32_TIMERLOW)
fileData.addPublicFunctions(TIMER_READTIMER32)


CHECKALARMN_DESCR = \
"\
 * @return \n\
 *         0: if the alarm is not triggered.\n\
 *         1: if the alarm is triggered."

# Std_ReturnType Timer_RP2040_CheckAlarm ( uint8 n );
TIMER_CHECKALARMN = function()
TIMER_CHECKALARMN.setFuncName(FUNC_PREFIX + "CheckAlarmN")
TIMER_CHECKALARMN.setDescription("Checks alarm 'n' to see if it has been triggered yet. Returns '1' if")
TIMER_CHECKALARMN.setBrief("Reads the timer from TIMER_TIMERAWL - stores the result in the buffer provided.")
TIMER_CHECKALARMN.setReturnType("uint8")
TIMER_CHECKALARMN.setReturnDesc(CHECKALARMN_DESCR)
TIMER_CHECKALARMN.setPreCondition("n/a")
TIMER_CHECKALARMN.setPostCondition("n/a")
TIMER_CHECKALARMN_INDEX = parameter()
TIMER_CHECKALARMN_INDEX.setBrief("Index of Alarm to be disarmed, must be within range [0:3].")
TIMER_CHECKALARMN_INDEX.setName("alarmIndex")
TIMER_CHECKALARMN_INDEX.setType(" uint8 ")
TIMER_CHECKALARMN.addParameter(TIMER_CHECKALARMN_INDEX)
fileData.addPublicFunctions(TIMER_CHECKALARMN)

# Std_ReturnType Timer_RP2040_DisarmAlarm ( uint8 n );
TIMER_DISARMALARMN = function()
TIMER_DISARMALARMN.setFuncName(FUNC_PREFIX + "DisarmAlarmN")
TIMER_DISARMALARMN.setDescription("Disables the alarm indicated by index 'alarmIndex'. rites to the TIMER_ARMED register to disarm the alarm indicated by the 'alarmIndex'. Reports OK if successful, and NOT_OK if failed. Checks input parameter is within range [0:3]")
TIMER_DISARMALARMN.setBrief("Writes to the TIMER_ARMED register to disarm the alarm indicated by the 'alarmIndex'.")
TIMER_DISARMALARMN.setReturnType("Std_ErrorCode")
TIMER_DISARMALARMN.setReturnDesc(STANDARD_RETURN_DESCR)
TIMER_DISARMALARMN.setPreCondition("n/a")
TIMER_DISARMALARMN.setPostCondition("n/a")
TIMER_DISARMALARMN_INDEX = parameter()
TIMER_DISARMALARMN_INDEX.setBrief("Index of Alarm to be checked, must be within range [0:3].")
TIMER_DISARMALARMN_INDEX.setName("alarmIndex")
TIMER_DISARMALARMN_INDEX.setType(" uint8 ")
TIMER_DISARMALARMN.addParameter(TIMER_DISARMALARMN_INDEX)
fileData.addPublicFunctions(TIMER_DISARMALARMN)
