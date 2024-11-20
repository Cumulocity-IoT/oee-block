# Developer Guide - Modify Inputs

## Rename inputs
If you want to change the names that are used on the block inputs without changing the calculation logic, it is sufficient to change the **@$inputName** in the comment of the [$process](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L445) action.

## Add additional inputs
If you require additional inputs that should be taken into account, first modify the signature and the comment of [$process](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L445) to add the additional inputs.

Then, you have to identify if the additional input is used for amount-based calculations or for state-based calculation. For amount-based calculations, it is expected that the input is a float and calculation adds individual inputs and splits them across intervals if required. For state-based calculation, it is expected that the input is a boolean and the calculation adds up the time in an interval when the input was true.

## Amount-based Calculation
For amount-based calculation it is very likely that you can reuse the existing  [applyToTransformationRule](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L229) action. It expects a [StatefulExpressionParser](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/eventdefinitions/ExpressionParser.mon#L406), which is used to keep track of the received amount and to split them across intervals. This object should be kept in the block state and is currently being initialized in the [setupCalculation](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L124) action for the existing inputs. 

## State-based Calculation
For state-based calculation it is likely that you need to implement more of the logic yourself. The basic calculation logic is implemented in the [TimeInStateExpressionParser](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/eventdefinitions/ExpressionParser.mon#L360) which calculates the time the condition evaluated to true.

The current OEE calculation contains two different cases for state-based calculation. [applyToMachineStatus](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L173) is the implementation for availability based on machine status. It is relatively straight-forward as availability can be calculated independently.

[applyToQualityStatus](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L204) is the more complex calculation of quality amounts based on quality status input. Instead of calculation the time, the quality status was ok, it needs to add amounts conditionally based on whether the current status is good or bad quality. It does so using an [AmountByQualityState](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/eventdefinitions/ExpressionParser.mon#L451) object.