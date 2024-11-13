__pysys_title__   = r""" Category Base - Base tests path 1 (APT, APA, AQA) """ 
#                        ================================================================================
__pysys_purpose__ = r""" """ 
	
__pysys_created__ = "2024-11-07"

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
							  # OEE=100
							  self.inputEvent('status', True, id=modelId),
                              self.timestamp(90),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),
                              self.timestamp(150),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),
                              self.timestamp(210),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),
                              self.timestamp(270),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),
							  # Availability=50
							  self.timestamp(300),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(330),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  self.timestamp(360),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(390),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  # Quality=50
							  self.timestamp(450),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  self.timestamp(510),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  # Performance=50
							  self.timestamp(570),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  self.timestamp(630),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 5, id=modelId),
							  # Availabilty=50, Performance=50
							  self.timestamp(660),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(690),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 2.5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  self.timestamp(720),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(750),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 2.5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  # Availabilty=50, Quality=50
							  self.timestamp(780),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(810),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  self.timestamp(840),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(870),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  # Performance=50, Quality=50							  
							  self.timestamp(930),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  self.timestamp(990),
							  self.inputEvent('amount', 5, id=modelId),
							  self.inputEvent('amount_ok', 2.5, id=modelId),
							  # Availabilty=50, Performance=50, Quality=50
							  self.timestamp(1020),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(1050),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 2.5, id=modelId),
							  self.inputEvent('amount_ok', 1.25, id=modelId),
							  self.timestamp(1080),
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(1110),
							  self.inputEvent('status', True, id=modelId),
							  self.inputEvent('amount', 2.5, id=modelId),
							  self.inputEvent('amount_ok', 1.25, id=modelId),
							  # Quality=0
							  self.timestamp(1170),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
                              self.timestamp(1230),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
							  # Performance=0, Quality=0
							  self.timestamp(1290),
							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
                              self.timestamp(1350),
							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),                              							  
							  # Availability=0,Performance=0, Quality=0
							  self.inputEvent('status', False, id=modelId),
							  self.timestamp(1410),
							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),
                              self.timestamp(1470),
							  self.inputEvent('amount', 0, id=modelId),
							  self.inputEvent('amount_ok', 0, id=modelId),                              							  
							  self.inputEvent('status', True, id=modelId),
							  self.timestamp(1530),
							  self.inputEvent('amount', 10, id=modelId),
							  self.inputEvent('amount_ok', 10, id=modelId),

                              )
		correlator.flush()

	def validate(self):
		self.assertBlockOutput('timestamp', 	[90.0,	150.0,	210.0,	270.0,	330.0,	390.0,	450.0,	510.0,	570.0,	630.0,	690.0,	750.0,	810.0,	870.0,	930.0, 	990.0,	1050.0,	1110.0,	1170.0,	1230.0,	1290.0,	1350.0,	1410.0,	1470.0])
		self.assertBlockOutput('oee',		 	[1.0,	1.0,	1.0,	1.0,	0.5,	0.5,	0.5,	0.5,	0.5,	0.5,	0.25,	0.25,	0.25,	0.25,	0.25,	0.25, 	0.125,	0.125,	0.0,	0.0,	0.0,	0.0,	0.0,	0.0])
		self.assertBlockOutput('availability', 	[1.0,	1.0,	1.0,	1.0,	0.5,	0.5,	1.0,	1.0,	1.0,	1.0,	0.5,	0.5,	0.5,	0.5,	1.0,	1.0,	0.5,	0.5,	1.0,	1.0,	1.0,	1.0,	0.0,	0.0])
		self.assertBlockOutput('performance', 	[1.0,	1.0,	1.0,	1.0,	1.0,	1.0,	1.0,	1.0,	0.5,	0.5,	0.5,	0.5,	1.0,	1.0,	0.5,	0.5,	0.5,	0.5,	1.0,	1.0,	0.0,	0.0,	0.0,	0.0])
		self.assertBlockOutput('quality', 		[1.0,	1.0,	1.0,	1.0,	1.0,	1.0,	0.5,	0.5,	1.0,	1.0,	1.0,	1.0,	0.5, 	0.5,	0.5,	0.5,	0.5,	0.5,	0.0,	0.0,	0.0,	0.0,	0.0,	0.0])

