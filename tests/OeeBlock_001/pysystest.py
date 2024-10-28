__pysys_title__   = r""" Category OEE - Basic OEE block test Path 1 (APT, APA, AQA) """ 
#                        ================================================================================
__pysys_purpose__ = r""" """ 
	
__pysys_created__ = "2024-04-07"

from apamax.analyticsbuilder.basetest import AnalyticsBuilderBaseTest
from pysys.constants import *

class PySysTest(AnalyticsBuilderBaseTest):
	def preInjectBlock(self, corr):
		AnalyticsBuilderBaseTest.preInjectBlock(self, corr)
		corr.injectEPL([self.project.APAMA_HOME +'/monitors/'+i+'.mon' for i in ['TimeFormatEvents']])
		corr.injectEPL([self.project.SOURCE +'/eventdefinitions/'+i+'.mon' for i in ['Util','Parser','OEEEventDefinitions', 'ExpressionParser']])
    
	def execute(self):
		correlator = self.startAnalyticsBuilderCorrelator(blockSourceDir=f'{self.project.SOURCE}/blocks/')
		modelId = self.createTestModel('apamax.analyticsbuilder.oee.Oee', 
								 inputs={'status':'boolean', 'pieces':'float', 'pieces_ok':'float' ,'pieces_nok':None,'qok':None},
								 parameters={'0:interval':60.0,'0:ica':10.0})	
		self.sendEventStrings(correlator,
                              self.timestamp(30),
							  self.inputEvent('status', True, id=modelId),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
                              self.timestamp(70),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(110),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(150),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
                              self.timestamp(190),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(230),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(270),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(310),
							  self.inputEvent('status', False, id=modelId),
                              self.inputEvent('pieces', 0, id=modelId),
							  self.inputEvent('pieces_ok', 0, id=modelId),
							  self.timestamp(350),
							  self.inputEvent('status', True, id=modelId),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(390),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(430),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(460),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(500),
                              )
		correlator.flush()

	def validate(self):
		self.checkLogs(warnIgnores=[f'Set time back to.*'])
		self.assertBlockOutput('timestamp', 	[90.0,	150.0,	210.0,	270.0,	330.0,		390.0,		450.0])
		self.assertBlockOutput('availability', 	[1.0,	1.0,	1.0,	1.0,	0.6667, 	0.6667, 	1.0])
		self.assertBlockOutput('performance', 	[0.5,	0.3,	0.3,	0.3,	0.15,	 	0.45, 		0.3333])
		self.assertBlockOutput('quality', 		[0.5,	0.5,	0.5,	0.5,	0.5,	 	0.5, 		0.5])
		self.assertThat('output == expected', 
						output=self.details('ActualProductionAmount'), 
						expected=				[5.0, 	3.0, 	3.0, 	3.0, 	1.0, 		3.0, 		3.3333])

	def details(self, selector, modelId='model_0', partitionId=None,time=None):
		return [evt['properties'][selector] for evt in self.apama.extractEventLoggerOutput(self.analyticsBuilderCorrelator.logfile)
			if evt['modelId'] == modelId and evt['outputId'] == 'details' and (partitionId == None or evt['partitionId'] == partitionId ) and (time == None or evt['time'] == time )]
