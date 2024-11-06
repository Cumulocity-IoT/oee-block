from apamax.analyticsbuilder.basetest import AnalyticsBuilderBaseTest
from pysys.constants import *

class OeeBaseTest(AnalyticsBuilderBaseTest):

	def preInjectBlock(self, corr):
		AnalyticsBuilderBaseTest.preInjectBlock(self, corr)
		corr.injectEPL([self.project.APAMA_HOME +'/monitors/'+i+'.mon' for i in ['TimeFormatEvents']])
		corr.injectEPL([self.project.SOURCE +'/eventdefinitions/'+i+'.mon' for i in ['Util','Parser','OEEEventDefinitions', 'ExpressionParser']])


	def details(self, selector, modelId='model_0', partitionId=None,time=None):
		return [evt['properties'][selector] for evt in self.apama.extractEventLoggerOutput(self.analyticsBuilderCorrelator.logfile)
			if evt['modelId'] == modelId and evt['outputId'] == 'details' and (partitionId == None or evt['partitionId'] == partitionId ) and (time == None or evt['time'] == time )]