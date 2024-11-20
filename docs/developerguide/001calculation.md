# Developer Guide - Modify OEE Calculation

## Understanding the high-level calculation logic

* Before the first calculation happens [setupCalculation](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L124) is called to configure how calculation happens. It does two things. First it calls [path](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L103), which checks what inputs are connected and selects the right calculation path based on the connected inputs. Second, based on the selected path the actual calculation is configured.
* [$process](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L445) is called on each received input during calculation. After determining which input was received the corresponding calculation logic is triggered. For any amount-based calculation [applyToTransformationRule](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L229) is called. For machine status [applyToMachineStatus](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L173) and for each quality status input [applyToQualityStatus](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L204) is called.
* Once values for all three configured inputs for a given interval are available, the corresponding *performOEECalculation_* actions is called. it performs all the intermediary calculations and returns a ***Value** object with the results.
* A timer is created for each interval for which a calculation result exists (with 0.1s delay between them) and the [$timerTriggered](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L515) action is invoked to send out the output.

## Modifying the calculation logic
The simplest modification is to modify the calculation logic. The action that is called for OEE calculation is assigned to the [oee_calculation](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L44C54-L44C69) action variable in the block state. You can either assign a different action to the variable or modify the existing calculations. 

At the moment, three variants of this action exist depending on which inputs are connected. For example, [performOEECalculation_APT_APA_AQA](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L293) does the calculation if the inputs are actual production time (through the machine status), actual production amount, and actual quality amount (either through the Amt Ok input or through the Quality Status input). 

The action received four float inputs and must return a Value object that contains properties for at least OEE, availability, performance, and quality.


