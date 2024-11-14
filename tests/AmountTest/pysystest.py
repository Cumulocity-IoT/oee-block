__pysys_title__   = r""" Category Amount - Tests focused on actual production amount """ 
#                        ================================================================================
__pysys_purpose__ = r""" """ 
	
__pysys_created__ = "2024-11-13"

from basetest.OeeBaseTest import OeeBaseTest
from pysys.constants import *
import basetest.OeeBaseTest

class PySysTest(OeeBaseTest):
    
	def execute(self):
		correlator = self.startAnalyticsBuilderCorrelator(blockSourceDir=f'{self.project.SOURCE}/src/blocks/oee')
		modelId = self.createTestModel('apamax.analyticsbuilder.oee.Oee', 
								 inputs={'status':'boolean', 'amount':'float', 'amount_ok':'float' ,'amount_nok':None,'qok':None},
								 parameters={'0:interval':60.0,'0:ica':10.0})	
		self.sendEventStrings(correlator,
                              self.timestamp(30),
							  # Splitting across multiple intervals
							  self.inputEvent('status', True, id=modelId),
  							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
							  self.timestamp(90),
							  self.inputEvent('status', True, id=modelId),
  							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),

                              self.timestamp(750),
							  self.inputEvent('status', True, id=modelId),
  							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),
                              self.timestamp(810),
                              )
		correlator.flush()

	def validate(self):
		self.assertBlockOutput('timestamp', 	[90.0,	150.0,	210.0,	270.0,	330.0,	390.0,	450.0,	510.0,	570.0,	630.0,	690.0,	750.0])
		self.assertThat('output == expected', 
						output=self.details('ActualProductionAmount'), 
						expected=				[5.0, 	3.0, 	3.0, 	3.0, 	0.0, 		4.0, 		3.3333])
