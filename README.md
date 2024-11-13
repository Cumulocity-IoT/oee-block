# Introduction

**OEE (Overall Equipment Effectiveness)** is a metric for measuring the efficiency, effectiveness and performance of production processes, by breaking them down into the three components Availability, Performance, and Quality.

This repository contains a custom block for the Analytics Builder that performs OEE calculations.

## Installation

To add this block to a tenant, you will require:

* A copy of the [block-sdk](https://github.com/SoftwareAG/apama-analytics-builder-block-sdk) github repo
* A local install of Apama - from either the SoftwareAG suite installer or [Community edition - full version](http://www.apamacommunity.com/downloads/).
* A Cumulocity IoT tenant with a suitable apama-ctrl microservice subscribed (custom blocks are not supported with apama-ctrl-starter).

Installation Steps:

```
. $SAG_INSTALL/Apama/bin/apama_env
./apama-analytics-builder-block-sdk/analytics_builder build extension \
      --input oee-block/src/  --name oee\
      --cumulocity_url https://$TENANT/ \
      --username $USERNAME --password $PASSWORD --restart
```

## User Documentation
Can be found [here](https://github.com/Cumulocity-IoT/oee-block/blob/main/docs/contents.md#user-guide).
## How to contribute
For any bugs or feature requests, please raise a ticket on the GitHub repository.

If you want to contribute to the block, please fork the the repository and follow the [Developer Guide](https://github.com/Cumulocity-IoT/oee-block/blob/main/docs/contents.md#developer-guide).

## Licensing

This project is licensed under the Apache 2.0 license - see <https://www.apache.org/licenses/LICENSE-2.0>

______________________
These tools are provided as-is and without warranty or support. They do not constitute part of the Software AG product suite. Users are free to use, fork and modify them, subject to the license agreement. While Software AG welcomes contributions, we cannot guarantee to include every contribution in the master project.
