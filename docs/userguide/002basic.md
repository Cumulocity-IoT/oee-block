# User Guide Basic Usage
Let us now create an Analytics Builder model to calculate OEE for a machine. A good starting point is the **Normal #1** simulator from the [oee-simulators](https://github.com/Cumulocity-IoT/oee-simulators) project, which produces the following data:

* **Availability**: the simulator produces an `Availability` event which has a field `status` that is either `up` or `down`. This event is produced 5-10 times per hour with 90% being `up`.
* **Performance**: the simulator produces an event `Piece_Produced`. The event is produced about 25 times per hour. 
* **Quality**: the simulator produces a `Piece_Ok` event. The event is produced about 20 times per hour. Those events follow a few seconds after a corresponding `Piece_Produced` event (both events have the same timestamp). Some `Piece_Produced` events are not followed by a `Piece_Ok` event (to simulate a piece with bad quality).

With this data available, we should connect the following inputs of the OEE block

* **Machine Status** to logic evalualting the status field of the `Availability` event
* **Amount** to logic counting the `Piece_Produced` events
* **Amt Ok** to logic counting the `Piece_Ok` events

## Step 1 - Block configuration
Reading the description of the simulator above carefully, tells us that it produces 25 pieces per hour, so configuring it to calculate OEE once per hour with an ideal piece count of 25 probably makes the most sense:
![Step 1 - Parameters](/docs/images/blockparameters.png)

## Step 2 - Availability calculation
Next, for availability calculation, the **Machine Status** input should be connected. It expects a Boolean input, so the `Availability` event cannot be used directly. Instead we first have to extract the value from its `status` field (using the **Extract Property** block) and compare its value to `up` (using the **Expression** block) to determine if the machine is running or not. The result should look like this:

![Step 2 - Availability](/docs/images/step2availability.png)

## Step 3 - Performance calculation
For performance calculation, the OEE block expects to receive piece counts on it **Amount** input. As we receive `Piece_Produced` events for every single produced piece, we need to convert each event into a count of a single piece. This is achieved using the **Constant Value** block:

![Step 3 - Performance](/docs/images/step3performance.png)


## Step 4 - Quality calculation
Quality calculation follows the same pattern like performance calculation but using the `Piece_Ok` events connected to the **Amt Ok** input:

![Step 4 - Quality](/docs/images/step4quality.png)


## Step 5 - Connecting to output
As a last step, the outputs of the OEE calculation should do something meaningful. In our case, we want to write OEE, availability, performance, and quality as measurements on the original device. For this purpose, the corresponding outputs of the OEE block can be connected directly to the value inputs of Measurement Output blocks. The timestamp output should be connected to the time input of the output blocks to ensure that the calculation is associated with the correct interval. The result should look like this:

![Step 5 - Output](/docs/images/step5output.png)

## Next steps
The above steps demonstrated how to get from raw device data to hourly OEE calculations. In the next section more [Advanced Scenarios](userguide/003advanced.md)  will be shown.

