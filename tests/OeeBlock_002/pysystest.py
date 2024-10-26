__pysys_title__   = r""" Category OEE - Basic OEE block test Path 2 """ 
#                        ================================================================================
__pysys_purpose__ = r""" """ 
	
__pysys_created__ = "2024-04-07"

from apamax.analyticsbuilder.basetest import AnalyticsBuilderBaseTest
from pysys.constants import *

class PySysTest(AnalyticsBuilderBaseTest):
	def execute(self):
		correlator = self.startAnalyticsBuilderCorrelator(blockSourceDir=f'{self.project.SOURCE}/blocks/')	
		modelId = self.createTestModel('apamax.analyticsbuilder.oee.Oee', 
								 inputs={'status':'boolean', 'pieces':'float', 'pieces_ok':None ,'pieces_nok':None,'qok':'boolean'},
								 parameters={'0:interval':600.0,'0:ica':10.0})	
		correlator.flush()

	def validate(self):
		self.checkLogs(warnIgnores=[f'Set time back to.*'])
