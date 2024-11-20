# Developer Guide - Modify Outputs

## Additional outputs
At the moment, the OEE block outputs OEE, availability, performance, and quality as individual outputs and the all intermediary calculations as properties on the **Details** output. Additional outputs can be introduced by declaring additional outputs on the block (see [Block SDK](https://github.com/Cumulocity-IoT/apama-analytics-builder-block-sdk/blob/main/doc/010-BasicBlocks.md) documentation for details) and setting them in the [$timerTriggered](https://github.com/Cumulocity-IoT/oee-block/blob/d150b0fa5eb201a93dd6f29e117840eac1cf37d6/src/blocks/oee/oee.mon#L515) action.

## Additional outputs from modified calculation
By [modifying the OEE calculation](developerguide/001calculation.md) the calculation can be changed to provide additional outputs. These can then be added like documented above.