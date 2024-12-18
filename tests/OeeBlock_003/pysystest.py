__pysys_title__   = r""" Category OEE - Basic OEE block test Path 3 (APT, AQA, QLA) """ 
#                        ================================================================================
__pysys_purpose__ = r""" """ 
	
__pysys_created__ = "2024-04-07"

from basetest.OeeBaseTest import OeeBaseTest
from pysys.constants import *

class PySysTest(OeeBaseTest):
    
	def execute(self):
		correlator = self.startAnalyticsBuilderCorrelator(blockSourceDir=f'{self.project.SOURCE}/src/blocks/oee')
		modelId = self.createTestModel('apamax.analyticsbuilder.oee.Oee', 
								 inputs={'status':'boolean', 'amount':None, 'amount_ok':'float' ,'amount_nok':'float','qok':None},
								 parameters={'0:interval':60.0,'0:ica':10.0})	
		self.sendEventStrings(correlator,
                              self.timestamp(30),
							  self.inputEvent('status', True, id=modelId),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
                              self.timestamp(70),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(110),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(150),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
                              self.timestamp(190),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(230),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(270),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(310),
							  self.inputEvent('status', False, id=modelId),
                              self.inputEvent('amount_nok', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
							  self.timestamp(350),
							  self.inputEvent('status', True, id=modelId),
							  self.timestamp(360),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(390),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(430),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(460),
                              self.inputEvent('amount_nok', 1, id=modelId),
							  self.inputEvent('amount_ok', 2, id=modelId),
							  self.timestamp(500),
                              )
		correlator.flush()

	def validate(self):
		self.assertBlockOutput('timestamp', 	[90.0,		150.0,	210.0,	270.0,	330.0,		390.0,		450.0])
		self.assertBlockOutput('availability', 	[1.0,		1.0,	1.0,	1.0,	0.6667, 	0.6667, 	1.0])
		self.assertBlockOutput('performance', 	[0.75,		0.45,	0.45,	0.45,	0.0,	 	0.9, 		0.5])
		self.assertBlockOutput('quality', 		[0.6667,	0.6667,	0.6667,	0.6667,	0.0,	 	0.6667, 	0.6667])
		self.assertThat('output == expected', 
						output=self.details('ActualProductionAmount'), 
						expected=				[7.5, 		4.5, 	4.5, 	4.5, 	0.0, 		6.0, 		5.0])
