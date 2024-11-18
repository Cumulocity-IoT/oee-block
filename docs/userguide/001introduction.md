# User Guide - Introduction
After following the installation instructions and restarting the apama-ctrl microservice, the OEE block is available in the **Aggregate** category and looks like this:

![OEE model](/docs/images/blockoverview.png)

## Block Parameters
The OEE block provides two parameters to configure its behavior:

* **Interval** - The interval for which the OEE should be calculated. Only a single interval can be configured. If more intervals are required, you can create several copies of the model or use template parameters to configure multple instances.
* **Ideal Cycle Amount** - The theoretical maximum that can be produced in a single interval. This is the baseline for the **performance** calculation. If the ideal cycle amount is produced in an interval, performance for that interval is 1.0 or 100%.

Note that both parameters are related to each other. The ideal cycle amount is defined for the configured interval length. If you increase the interval length from 10 minutes to 60 minutes you should increae the ideal cycle amount proportionally. 

## Block Inputs
The block calculates OEE by processing inputs about equipment availability, amount produced and the quality of the produced amount. For this a subset of the inputs of the block need to be connected:

* **Machine Status** - availability indicator (true / false)
* **Amount** - produced amount (total)
* **Amt Ok** - produced amount of good quality
* **Amt NOk** - produced amount of bad quality
* **Quality Ok** - quality indicator (true/false)

The Machine Status must always be provided, for the other three parameters the following combinations are allowed:
* Amount + Amt Ok
* Amount + Quality Ok
* Amt Ok + Amt NOk
* Amount + Amt Ok

## Block Outputs
Once for every interval, the block provides updated values on all its outputs. All outputs are produced with the same
activation an belong together:

* **OEE	The calculated** - OEE for the interval.
* **Availability** - The calculated availability for the interval.
* **Performance** - The calculated performance for the interval.
* **Quality** - The calculated quality for the interval.
* **Timestamp** - The timestamp marking the end of the calculated interval.
* **Details** - All components of the OEE calculation in the form of a pulse output: OEE, Availability, Performance, Quality, Actual Production Amount, Actual Production Time, Actual Quality Amount, Ideal Amount, Ideal Cycle Time, Ideal Qualiy Time, Ideal Machine Runtime, Quality Loss Amount, Availability Loss Amount, Performance Loss Amount, Performance Loss Time, Quality Loss Time, Availability Loss Time.

## Understanding asynchronous output
The OEE block provides output once for each interval representing the calculated OEE value for that interval. This value will be produced at some point in time after the interval concluded. As explained in the OEE theory section [here](oee-theory/004splitting.md), the OEE block splits amount proportionally to the intervals to which the amount relate. To be able to do this, the OEE calculation can only be concluded once an amount input is received for each of the configured amounts after the interval concluded.

This means that the activation timestamp of the output will typically be significantly after the timestamp of the interval. The timestamp of the interval is delivered as a separate output and should be used whenever the time of the calculated OEE is important. For example, when producing measurements, the timestamp output of the OEE block should be connected to the time input of the Measurement Output block to produce measurements for the correct timestamp.

If another Analytics Builder model should use the results of a model using the OEE block, it is very likely that the input blocks of that model should have **Ignore Timestamp** enabled and the logic of the model should anticipate getting inputs out of line with the activation timestamps.

If no data is received for multiple intervals (e.g. at night), on receiving the next data multiple intervals will be closed. The OEE block sends the data of these intervals in order with a 0.1s wait time between activations.
