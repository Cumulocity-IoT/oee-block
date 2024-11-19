# Advanced Scenarios
This section shows some examples of more complex behavior that can be achieved with the OEE block.

## Raising Alarms on Outputs
A straightforward modification to the simple model, is to raise an alarm instead or in addition to producing measurements. This can either be achieved with a smart rule or if you require more flexibility in the same Analytics Builder model using for exmaple the **Threshold** block (though the **Expression** or **Range** blocks should work similarly). It is important to use the timestamp output as the alarm timestamp so that the alarm is raised at the right point in time.

![Alarm Output](/docs/images/alarmoutput.png)

## Additional Mapping of Inputs
The simple example counted events to determine performance and quality but you can use the full power of Analytics Builder to prepare the input data. IF you used the  **Normal #2** simulator from the [oee-simulators](https://github.com/Cumulocity-IoT/oee-simulators) project, it uses `Pieces_Produced` and `Pieces_Ok` events which each contain the count of produced and of good pieces. So instead of counting events, you have to extract the counts from the events using the **Extract Property** block. Make sure to select float as the property type.

![Extract counts](/docs/images/normal2.png)

## Extracting Additional Outputs
In addition to the calculated OEE value and its subcomponents availability, performance, and quality, the OEE block also provides all intermediary calculation results. These are: OEE, Availability, Performance, Quality, Actual Production Amount, Actual Production Time, Actual Quality Amount, Ideal Amount, Ideal Cycle Time, Ideal Quality Time, Ideal Machine Runtime, Quality Loss Amount, Availability Loss Amount, Performance Loss Amount, Performance Loss Time, Quality Loss Time, Availability Loss Time.

Each of them is available as a property on the Details output of the OEE block and can be extracted using the **Extract Property** block. Property names are without spaces, so `Actual Production Amount` is available via the property `ActualProductionAmount`. Extracted values can be used just like the other outputs to create measurements or raise alarms. Without extracting the properties, the Details output can be used as the Properties input of an Event Output block to write all intermediary calculation results into a single event.

## Group OEE
Calculating the OEE of a group of devices can be achieved through various means. The simplest one is probably to use the **Group Statistics** block to calculate an average OEE. For this to work properly, the devices need to be assigned to an asset in Cumulocity Digital Twin Manager and the asset should be used as input (selecting device's assets) and output of the model. To avoid running into Analytics Builder complaining about loops, the fragment and series of the output should be different than the input (e.g. by using OEE_avg as the output series).

![Group OEE](/docs/images/groupoee.png)

If the group of devices is a line, calculating the average probably does not make much sense. The **Expression** block could be used to calculate the product of the individual device OEEs. If all device contribute to the OEE differently, the OEE block could use data from different devices. Availability could be derived by combining the individual device status using the logical blocks **AND**, **OR**, and **NOT**. Data from one device could be used as the amount input for performance calculation and another machine could be used to calculate ok or faulty pieces.

## Shift Plans
Shift plans allow to control when OEE is calculated. The OEE block does not support shift plans out of the box but they can be achieved using other blocks. Below example uses **Cron Timer** blocks scheduled at 8:00am and 4:00pm to open and close a **Gate** block. The gated value is the amount for the performance calculation of the OEE block. The **Gate** block is configued with a null value of 0 meaning that at 4:00pm each day an amount of 0 is sent to finalize the last calculation.

![Shift Plan using Cron Timer](/docs/images/shiftplan.png)

Note that the OEE block would still create OEE calculation results for the time between 4:00pm and 8:00am. These would be created after 8:00am when the first data of the morning is received. To avoid this, a separate **Gate** block could disable outputs during that time.

Besides using **Cron Timer** the information to start and end shifts can also come as measurements or events or from other data sources using custom blocks.

## Production Plans
Production plans define what is being produced in what quantity at what time. Currently, the OEE App does not support production plans directly as the ideal cycle amount is configured as a parameter. A workaround is to have multiple models or to use a template parameter for the ideal cycle amount and have multiple instances of the model and to control when each model is calculating OEE using similar mechanisms like the ones employed for shift plans above. This will only work if production plans are more or less stable.