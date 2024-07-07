/**
 * 
* @file "Timer_RP2040.h"
* @author Madrick3
* @brief Provides a global timebase for software through the generation of a global microsecond timebase. The timebase relies
* on a  one microsend reference that is generated in the watchdog, and is derived from the reference clock (REFCLK).
* A 64-bit timer is managed, and is not able to overflow on it's own - thoughtful use of the module provides
* completely monotic use in practice. Otherwise, the module initializes, manages, and clears the timer, also manages
* the alarms which may trigger interrupts.
* 
* @COMPONENT: TIMER_RP2040
* @VERSION: 00.01.00 
*/
/************************************************************
  Version History
  -----------------------------------------------------------
  Revision |  Author   |  Change ID  |  Description
  00.00.00 |  AUTHOR   |  DRAFT      |  Initial Creation
************************************************************/

/************************************************************
  DEFINES
************************************************************/

/************************************************************
  INCLUDES
************************************************************/
#include "Platform_Types.h"
#include "Timer_RP2040_SFR.h"

/************************************************************
  ENUMS AND TYPEDEFS
************************************************************/

/************************************************************
  EXTERN FUNCTIONS
************************************************************/

/************************************************************
  GLOBAL FUNCTIONS
************************************************************/

/**
 * Initializes the timer module for a basic runtime implemetations: Arms ALARM0 as a 1ms timer, clears TIME, and begins
 * the timer. Can fail if the RP2040_Watchdog is not already initialized. (See RP2040 datasheet section 4.7.2 'Tick
 * Generation'). Interrupts are not necessarily enabled at this stage.
 *
 * @return 
 *         0: 'E_OK' if successful 
 *         1: 'E_NOT_OK' if the operation is not successful
 *
 * @pre  Tick generation is already started in the watchdog module. 
 * @post  ALARM0 is armed. 
 * @invariant n/a
 *
 */
extern Std_ErrorCode Timer_RP2040_Init ( void );

/**
 * Updates internal tracking variables that the timer is 'uninit'. Disables all alarms. Pauses the timer. Expects that
 * the timer module was previously enabled, and will report an error if the module was not initialized. Will disable
 * interrupts as well.
 *
 * @return 
 *         0: 'E_OK' if successful 
 *         1: 'E_NOT_OK' if the operation is not successful 
 *         3: 'E_MODULE_UNINIT' if the timer is not yet initialized
 *
 * @pre Timer module was previously enabled.
 * @post Alarms are all disabeled, Timer is paused.
 * @invariant n/a
 *
 */
extern Std_ErrorCode Timer_RP2040_Deinit ( void );

/**
 * 
 *
 * @return 
 *         0: 'E_OK' if successful 
 *         1: 'E_NOT_OK' if the operation is not successful 
 *         3: 'E_MODULE_UNINIT' if the timer is not yet initialized
 *
 * @pre Timer module was previously enabled.
 * @post Alarms are all disabeled, Timer is paused.
 * @invariant n/a
 *
 */
extern Std_ErrorCode Timer_RP2040_InterruptEnable ( void );

