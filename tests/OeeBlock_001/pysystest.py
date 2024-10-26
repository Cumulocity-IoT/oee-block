__pysys_title__   = r""" Category OEE - Basic OEE block test Path 1 """ 
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
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(350),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(390),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(430),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
							  self.timestamp(470),
                              self.inputEvent('pieces', 2, id=modelId),
							  self.inputEvent('pieces_ok', 1, id=modelId),
  							  self.inputEvent('status', True, id=modelId),
                              )
		
		correlator.flush()

	def validate(self):
		self.checkLogs(warnIgnores=[f'Set time back to.*'])
