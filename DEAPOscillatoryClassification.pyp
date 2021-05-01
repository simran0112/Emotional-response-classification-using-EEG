<?xml version='1.0' encoding='utf-8'?>
<scheme description="Neural oscillations indicate various neural activities or neural states, such as, relaxation, emotions, cognitive processing, and motor control. This pipeline provides the core processing required to extract such neural oscillatory patterns in the context of classification between possible categories or scenarios.&#10;&#10;The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations. Some of the available CSP algorithms in NeuroPype are: CSP and Filterbank CSP which are mostly targeted for classification algorithms and Source Power Comodulation (SPoC) and Filterbank SPoC which are targeted for regression algorithms.&#10;&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import Test Data” and “Import Calibration Data”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Test Data” and “Import Calibration Data”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here with data recorded with Cognionics headset that the last 5 channels are not used and are removed.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 8-28 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Filter Bank Common Spatial Patterns (FBCSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions. In the FBCSP method, multiple frequency bands can be defined and then desired number of filters are designed for each frequency band. These filters are then applied to the data to extract the features corresponding to model patterns. &#10;You can define the frequency bands of interest for this node. Also, you can choose different windows for frequency calculation in order to avoid the boundary effect.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. For example  you can  use the misclassification rate (MCR) or area under the curve (AUC)." title="Oscillatory process classification" version="2.0">
	<nodes>
		<node id="0" name="FIR Filter" position="(197.0, 302.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="e74911dd-3f6d-4071-8dea-aa873888dedf" version="1.0.0" />
		<node id="1" name="Segmentation" position="(300, 300)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="6fd7ccba-3998-4f33-87f3-6994253234a1" version="1.0.1" />
		<node id="2" name="Variance" position="(500, 300)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="02f46fbf-dc00-4a39-b18a-4e78c2683608" version="1.0.0" />
		<node id="3" name="Logistic Regression" position="(702.0, 49.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="e7c7692f-b21c-4755-8015-ffa322d52a5e" version="1.0.0" />
		<node id="4" name="Assign Target Values" position="(500, 100)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="37d61b72-2810-4e5e-8c2c-a9e00f67f954" version="1.0.0" />
		<node id="5" name="Logarithm" position="(600, 300)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="fe52b38a-25d1-4407-a062-2acbd0d54cd2" version="1.0.0" />
		<node id="6" name="Dejitter Timestamps" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="2b52573f-2f7e-4cfa-9316-2f3d4f15bd2f" version="1.0.0" />
		<node id="7" name="Select Range" position="(600, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="1d3a3fcf-a089-4009-a465-ae787997c410" version="1.0.0" />
		<node id="8" name="Inject Calibration Data" position="(400, 100)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="2a90fa36-aff8-480d-aaa4-8d0f71ba25d9" version="1.0.0" />
		<node id="9" name="Stream Data" position="(200, 500)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="17f9f59a-09c3-4813-80e7-79c600b3f682" version="1.1.0" />
		<node id="10" name="LSL Output" position="(300, 500)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="0e2ea86a-0758-4f2b-8713-b91d68a7f1f9" version="1.0.0" />
		<node id="11" name="LSL Input" position="(100, 100)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="fb1e3721-795e-48cc-b108-5e792b869355" version="1.0.0" />
		<node id="12" name="LSL Output" position="(967.0, 31.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="bbbdabce-9154-46a8-adb6-83a199287ab6" version="1.0.0" />
		<node id="13" name="Filter Bank Common Spatial Patterns" position="(403.0, 299.0)" project_name="NeuroPype" qualified_name="widgets.neural.owfilterbankcommonspatialpattern.OWFilterBankCommonSpatialPattern" title="Filter Bank Common Spatial Patterns" uuid="2aeb11da-cd22-458e-bdfc-fbffd8ec6735" version="1.0.0" />
		<node id="14" name="Streaming Bar Plot" position="(1002.0, -37.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="06d617cd-460b-4a84-9b89-fdab04d9dfa3" version="1.0.2" />
		<node id="15" name="Override Axis" position="(794.0, -35.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="a0335d71-e54b-4aac-9540-20feb1738039" version="1.0.2" />
		<node id="16" name="Mean" position="(899.0, -37.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="32cc0e60-a4a9-4ac7-8b74-38c0303fb367" version="1.0.0" />
		<node id="17" name="Import CSV" position="(87.0, 501.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportcsv.OWImportCSV" title="Import CSV" uuid="7f652bfb-9339-405e-ad14-4aec2ff732a0" version="1.0.1" />
		<node id="18" name="Import CSV" position="(106.0, -5.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportcsv.OWImportCSV" title="Import CSV (1)" uuid="3cf1f3e9-1415-4102-a563-8fbd7b79fe66" version="1.0.1" />
		<node id="19" name="Measure Loss" position="(1133.0, 391.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owmeasureloss.OWMeasureLoss" title="Measure Loss" uuid="685cd964-e1ba-4e81-ac26-9fd759d9bfec" version="1.0.2" />
		<node id="20" name="Time Series Plot" position="(428.0, 506.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot (1)" uuid="2e589c55-86b4-46a4-bd04-c38901a91517" version="1.0.1" />
		<node id="21" name="Print To Console" position="(1247.0, 390.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="4de354a5-9959-4858-a100-58037d8c0780" version="1.0.0" />
		<node id="22" name="Power Spectrum (Welch)" position="(432.0, 412.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" title="Power Spectrum (Welch)" uuid="07ad03ba-8b33-4d43-b470-4b13b6ef77f3" version="1.0.0" />
		<node id="23" name="Spectrum Plot" position="(546.0, 412.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" title="Spectrum Plot" uuid="ab336258-99d8-41b7-af98-3e54499b41b5" version="1.0.0" />
		<node id="24" name="Record to CSV" position="(822.0, 70.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="e89f1352-58cf-43e4-bfb7-b490a32227d2" version="1.0.0" />
		<node id="25" name="Support Vector Classification" position="(716.0, 235.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owsupportvectorclassification.OWSupportVectorClassification" title="Support Vector Classification" uuid="43ac7ab1-bd6b-49ee-8a88-3332b22479de" version="1.0.0" />
		<node id="26" name="Quadratic Discriminant Analysis" position="(707.0, 565.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owquadraticdiscriminantanalysis.OWQuadraticDiscriminantAnalysis" title="Quadratic Discriminant Analysis" uuid="a4a0981e-b187-4e0b-85b1-d7f244ffbb9b" version="1.0.0" />
		<node id="27" name="Linear Discriminant Analysis" position="(710.0, 375.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="ae5098f8-4671-4bb1-bddf-cfc3b4cfcdd2" version="1.0.0" />
		<node id="28" name="Override Axis" position="(829.0, 527.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="11b7798c-fafd-471c-87c1-96058c8e7b6d" version="1.0.2" />
		<node id="29" name="Override Axis" position="(821.0, 346.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="abf345bc-38bf-424e-a031-dbe9ae589cd1" version="1.0.2" />
		<node id="30" name="Override Axis" position="(815.0, 157.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="c0e02d83-9728-4fb0-8bb3-d36e429570b3" version="1.0.2" />
		<node id="31" name="Mean" position="(921.0, 156.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="835839c5-8ab6-4b88-938a-bfcca5e5596a" version="1.0.0" />
		<node id="32" name="Streaming Bar Plot" position="(1024.0, 154.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="61210659-96f4-48e4-9441-04a56860bb33" version="1.0.2" />
		<node id="33" name="Mean" position="(917.0, 345.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="b79581fa-1e80-47b9-95c7-2cf9bda02717" version="1.0.0" />
		<node id="34" name="Streaming Bar Plot" position="(1033.0, 343.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="f850c0e6-f79f-4ebd-812d-096894be9d67" version="1.0.2" />
		<node id="35" name="Mean" position="(935.0, 526.0)" project_name="NeuroPype" qualified_name="widgets.statistics.owmean.OWMean" title="Mean" uuid="f4568184-28fa-4c2f-8b0a-892d4e160896" version="1.0.0" />
		<node id="36" name="Streaming Bar Plot" position="(1042.0, 525.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="fde57fa6-d83d-4040-94c5-3f040785d798" version="1.0.2" />
		<node id="37" name="Record to CSV" position="(830.0, 266.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="8864f9dc-81da-4efd-8763-acf5fdcd6256" version="1.0.0" />
		<node id="38" name="Record to CSV" position="(830.0, 445.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="407ba5a0-ebd6-4107-b2eb-8ebd0508e8f2" version="1.0.0" />
		<node id="39" name="Record to CSV" position="(851.0, 653.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtocsv.OWRecordToCSV" title="Record to CSV" uuid="3e0e2b2a-0256-4d74-83c8-2aa293f1c787" version="1.0.0" />
		<node id="40" name="LSL Output" position="(989.0, 219.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="4055b631-0d38-4a7e-8d41-6413bce87aef" version="1.0.0" />
		<node id="41" name="LSL Output" position="(982.0, 418.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="e158d816-35b6-4376-9e4c-3d06896f7ed9" version="1.0.0" />
		<node id="42" name="LSL Output" position="(979.0, 626.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="24488188-1c06-425a-a6ca-47706f574d82" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="5" sink_channel="Streaming Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="9" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="14" sink_channel="Calib Data" sink_node_id="8" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="15" sink_channel="Data" sink_node_id="23" source_channel="Data" source_node_id="22" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="24" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="21" source_channel="Loss" source_node_id="19" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="13" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="25" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="30" source_channel="Data" source_node_id="25" />
		<link enabled="true" id="24" sink_channel="Data" sink_node_id="29" source_channel="Data" source_node_id="27" />
		<link enabled="true" id="25" sink_channel="Data" sink_node_id="28" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="26" sink_channel="Data" sink_node_id="32" source_channel="Data" source_node_id="31" />
		<link enabled="true" id="27" sink_channel="Data" sink_node_id="34" source_channel="Data" source_node_id="33" />
		<link enabled="true" id="28" sink_channel="Data" sink_node_id="36" source_channel="Data" source_node_id="35" />
		<link enabled="true" id="29" sink_channel="Data" sink_node_id="31" source_channel="Data" source_node_id="30" />
		<link enabled="true" id="30" sink_channel="Data" sink_node_id="33" source_channel="Data" source_node_id="29" />
		<link enabled="true" id="31" sink_channel="Data" sink_node_id="35" source_channel="Data" source_node_id="28" />
		<link enabled="true" id="32" sink_channel="Data" sink_node_id="37" source_channel="Data" source_node_id="25" />
		<link enabled="true" id="33" sink_channel="Data" sink_node_id="38" source_channel="Data" source_node_id="27" />
		<link enabled="true" id="34" sink_channel="Data" sink_node_id="39" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="35" sink_channel="Data" sink_node_id="27" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="36" sink_channel="Data" sink_node_id="26" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="37" sink_channel="Data" sink_node_id="42" source_channel="Data" source_node_id="26" />
		<link enabled="true" id="38" sink_channel="Data" sink_node_id="41" source_channel="Data" source_node_id="27" />
		<link enabled="true" id="39" sink_channel="Data" sink_node_id="40" source_channel="Data" source_node_id="25" />
		<link enabled="true" id="40" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="27" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEdAAAAAAAAAAEdAEAAAAAAAAEdARQAAAAAAAEdARoAAAAAAAGVY
DQAAAG1pbmltdW1fcGhhc2VxCYhYBAAAAG1vZGVxClgIAAAAYmFuZHBhc3NxC1gFAAAAb3JkZXJx
DFgNAAAAKHVzZSBkZWZhdWx0KXENWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ5jc2lwCl91bnBp
Y2tsZV90eXBlCnEPWAwAAABQeVF0NC5RdENvcmVxEFgKAAAAUUJ5dGVBcnJheXERQy4B2dDLAAEA
AAAAAbIAAAH4AAADLwAAAzMAAAG9AAACJQAAAyQAAAMoAAAAAAAAcRKFcROHcRRScRVYDgAAAHNl
dF9icmVha3BvaW50cRaJWAoAAABzdG9wX2F0dGVucRdHQEkAAAAAAAB1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYDQAAAG1hcmtlci1sb2NrZWRxBFgNAAAAc2FtcGxl
X29mZnNldHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUK
cQdYDAAAAFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAACtgAAATsA
AATfAAADNAAAAsEAAAFoAAAE1AAAAykAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtl
cnNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9i
b3VuZHNxEV1xEihLAEsFZVgHAAAAdmVyYm9zZXETiXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQVjc2lwCl91
bnBpY2tsZV90eXBlCnEGWAwAAABQeVF0NC5RdENvcmVxB1gKAAAAUUJ5dGVBcnJheXEIQy4B2dDL
AAEAAAAAAwIAAAGtAAAEeQAAAmIAAAMKAAABzAAABHEAAAJaAAAAAAAAcQmFcQqHcQtScQxYDgAA
AHNldF9icmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWAwAAABpbmNsdWRlX2JpYXNxCohYDwAA
AGluaXRpYWxpemVfb25jZXELiFgIAAAAbWF4X2l0ZXJxDEtkWAoAAABtdWx0aWNsYXNzcQ1YAwAA
AG92cnEOWAkAAABudW1fZm9sZHNxD0sFWAgAAABudW1fam9ic3EQSwFYDQAAAHByb2JhYmlsaXN0
aWNxEYhYCwAAAHJlZ3VsYXJpemVycRJYAgAAAGwycRNYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
FGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5
cRdDLgHZ0MsAAQAAAAAAAAAAATMAAAF9AAADaAAAAAsAAAFgAAABcgAAA10AAAAAAABxGIVxGYdx
GlJxG1gNAAAAc2VhcmNoX21ldHJpY3EcWAgAAABhY2N1cmFjeXEdWA4AAABzZXRfYnJlYWtwb2lu
dHEeiVgGAAAAc29sdmVycR9YBQAAAGxiZmdzcSBYCQAAAHRvbGVyYW5jZXEhRz8aNuLrHEMtWAkA
AAB2ZXJib3NpdHlxIksAdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYBAAAAGhpZ2hxB0sB
WAMAAABsb3dxCEsAdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29tcGF0cQpYEwAAAHNhdmVk
V2lkZ2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAAAFB5UXQ0LlF0Q29yZXEN
WAoAAABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAABDQAAAr8AAAKKAAAD7AAAARgAAALsAAACfwAA
A+EAAAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lYEQAAAHN1cHBvcnRfd2ls
ZGNhcmRzcRSJWAsAAAB1c2VfbnVtYmVyc3EViVgHAAAAdmVyYm9zZXEWiXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEDY3NpcApfdW5waWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRl
QXJyYXlxBkMuAdnQywABAAD///6IAAAB0f////8AAAJW///+kAAAAe/////3AAACTgAAAAAAAHEH
hXEIh3EJUnEKWA4AAABzZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQRjc2lwCl91bnBp
Y2tsZV90eXBlCnEFWAwAAABQeVF0NC5RdENvcmVxBlgKAAAAUUJ5dGVBcnJheXEHQy4B2dDLAAEA
AAAAAwIAAAGsAAAEfwAAAoYAAAMNAAAB2QAABHQAAAJ7AAAAAAAAcQiFcQmHcQpScQtYDgAAAHNl
dF9icmVha3BvaW50cQyJWA4AAAB3YXJtdXBfc2FtcGxlc3ENSv////91Lg==
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAAmAAAAJEAAAPRAAACVgAAAKMA
AAC+AAADxgAAAksAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAwAAADotMXENWA4A
AABzZXRfYnJlYWtwb2ludHEOiVgEAAAAdW5pdHEPWAcAAABpbmRpY2VzcRB1Lg==
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiFgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXECY3NpcApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRl
QXJyYXlxBUMuAdnQywABAAAAAAMCAAAB0QAABH8AAAKYAAADDQAAAf4AAAR0AAACjQAAAAAAAHEG
hXEHh3EIUnEJWA4AAABzZXRfYnJlYWtwb2ludHEKiXUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBR0AkAAAAAAAAWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSwVYBwAAAGxvb3BpbmdxA4lYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAAEAQAAAYMAAAV/AAADCwAABAwAAAGwAAAFdAAAAwAAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDktkWAkAAABzdGFy
dF9wb3NxD0cAAAAAAAAAAFgQAAAAdGltZXN0YW1wX2ppdHRlcnEQRwAAAAAAAAAAWAYAAAB0aW1p
bmdxEVgNAAAAZGV0ZXJtaW5pc3RpY3ESWA8AAAB1cGRhdGVfaW50ZXJ2YWxxE0c/pHrhR64Ue3Uu
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYFQAAAE91dFN0cmVhbURhdGEtbWFya2Vyc3EEWBAAAABtYXJrZXJfc291
cmNlX2lkcQVYAAAAAHEGWAwAAABtYXhfYnVmZmVyZWRxB0s8WBcAAAByZXNldF9pZl9sYWJlbHNf
Y2hhbmdlZHEIiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEJY3NpcApfdW5waWNrbGVfdHlwZQpx
ClgMAAAAUHlRdDQuUXRDb3JlcQtYCgAAAFFCeXRlQXJyYXlxDEMuAdnQywABAAAAAAMCAAABcgAA
BH8AAANuAAADDQAAAZ8AAAR0AAADYwAAAAAAAHENhXEOh3EPUnEQWAwAAABzZW5kX21hcmtlcnNx
EYhYDgAAAHNldF9icmVha3BvaW50cRKJWAkAAABzb3VyY2VfaWRxE1gNAAAAbXlzb3VyY2VpZDIz
NHEUWAUAAABzcmF0ZXEVWA0AAAAodXNlIGRlZmF1bHQpcRZYCwAAAHN0cmVhbV9uYW1lcRdYDQAA
AE91dFN0cmVhbURhdGFxGFgLAAAAc3RyZWFtX3R5cGVxGVgDAAAARUVHcRpYEwAAAHVzZV9kYXRh
X3RpbWVzdGFtcHNxG4hYFgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xHIl1Lg==
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgcAAAAbmFtZT0nT3V0U3RyZWFtRGF0YS1tYXJrZXJzJ3EFWAwAAABtYXhfYmxv
Y2tsZW5xBk0ABFgKAAAAbWF4X2J1ZmxlbnEHSx5YDAAAAG1heF9jaHVua2xlbnEISwBYDAAAAG5v
bWluYWxfcmF0ZXEJWA0AAAAodXNlIGRlZmF1bHQpcQpYBQAAAHF1ZXJ5cQtYFAAAAG5hbWU9J091
dFN0cmVhbURhdGEncQxYBwAAAHJlY292ZXJxDYhYFAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5H
P+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBY
DAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFycmF5cRJDLgHZ0MsAAQAAAAABwgAAAOYAAAM/
AAACMwAAAc0AAAETAAADNAAAAigAAAAAAABxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRx
F4l1Lg==
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAwIAAAFyAAAEfwAA
A24AAAMNAAABnwAABHQAAANjAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETWCoAAAAobmV2ZXIgdXNlIHNhbWUg
c291cmNlIGlkIGluIG9uZSBweXBlbGluZSlxFFgFAAAAc3JhdGVxFVgNAAAAKHVzZSBkZWZhdWx0
KXEWWAsAAABzdHJlYW1fbmFtZXEXWAkAAABPdXRTdHJlYW1xGFgLAAAAc3RyZWFtX3R5cGVxGVgH
AAAAQ29udHJvbHEaWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRuIWBYAAAB1c2VfbnVtcHlfb3B0
aW1pemF0aW9ucRyJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAUAAABiYW5kc3EBXXECKF1xAyhLBEsHZV1xBChLCEsMZV1xBShLDUseZV1xBihLH0sq
ZWVYCgAAAGNvbmRfZmllbGRxB1gLAAAAVGFyZ2V0VmFsdWVxCFgPAAAAaW5pdGlhbGl6ZV9vbmNl
cQmIWAwAAABtaW5fZmZ0X3NpemVxCk0AAlgDAAAAbm9mcQtLA1gOAAAAb3ZlcmxhcF9sZW5ndGhx
DFgNAAAAKHVzZSBkZWZhdWx0KXENWAwAAABvdmVybGFwX3VuaXRxDlgHAAAAc2FtcGxlc3EPWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NC5R
dENvcmVxElgKAAAAUUJ5dGVBcnJheXETQy4B2dDLAAEAAAAAApQAAABNAAAEEQAAAf4AAAKfAAAA
egAABAYAAAHzAAAAAAAAcRSFcRWHcRZScRdYDgAAAHNldF9icmVha3BvaW50cRiJWAkAAABzaHJp
bmthZ2VxGUsAWAsAAAB3aW5kb3dfZnVuY3EaWAQAAABoYW5ucRtYDQAAAHdpbmRvd19sZW5ndGhx
HGgNWAwAAAB3aW5kb3dfcGFyYW1xHWgNWAsAAAB3aW5kb3dfdW5pdHEeaA91Lg==
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/szMzMzMzNWAwAAABpbml0aWFsX2RpbXNxCV1xCihNIANLMk28Ak30
AWVYDgAAAGluc3RhbmNlX2ZpZWxkcQtYDQAAACh1c2UgZGVmYXVsdClxDFgOAAAAbGFiZWxfcm90
YXRpb25xDVgKAAAAaG9yaXpvbnRhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91
bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDL
AAEAAAAAAwQAAAEiAAAEgQAAAugAAAMPAAABTwAABHYAAALdAAAAAAAAcROFcRSHcRVScRZYDgAA
AHNldF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRlY
DQAAACh1c2UgZGVmYXVsdClxGlgFAAAAdGl0bGVxG1gXAAAATG9naXN0aWMgQ2xhc3NpZmljYXRp
b25xHFgRAAAAdXNlX2xhc3RfaW5zdGFuY2VxHYhYBwAAAHZlcmJvc2VxHohYCAAAAHlfbGltaXRz
cR9dcSAoSwBLAWV1Lg==
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4lYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHKFgLAAAAbG93IGFyb3VzYWxxCFgMAAAAaGlnaCBhcm91
c2FscQllWAgAAABuZXdfYXhpc3EKWAcAAABmZWF0dXJlcQtYCAAAAG9sZF9heGlzcQxYBwAAAGZl
YXR1cmVxDVgMAAAAb25seV9zaWduYWxzcQ6JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lw
Cl91bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B
2dDLAAEAAAAAAr4AAAFaAAAE1wAAAtgAAALJAAABhwAABMwAAALNAAAAAAAAcROFcRSHcRVScRZY
DgAAAHNldF9icmVha3BvaW50cReJdS4=
</properties>
		<properties format="literal" node_id="16">{'axis': 'instance', 'force_feature_axis': False, 'ignore_nans': False, 'robust': False, 'robust_estimator_type': 'median', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'trim_proportion': 0.1}</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWBAA
AABkYXRhX3N0cmVhbV9uYW1lcQdYAwAAAGVlZ3EIWA4AAABlbWl0X2VhY2hfdGlja3EJiVgPAAAA
ZXhjbHVkZV9jb2x1bW5zcQpdcQtYCAAAAGZpbGVuYW1lcQxYOwAAAEM6L1VzZXJzL1NpbXJhbi9E
ZXNrdG9wL01TL0JDSS9CQ0lQcm9qL0JDSVByb2ovRGF0YS9zMzIuY3N2cQ1YDwAAAGluY2x1ZGVf
Y29sdW1uc3EOXXEPWBQAAABpbnN0YW5jZV9jb2x1bW5fbmFtZXEQaAJYDQAAAG1hcmtlcl9jb2x1
bW5xEVgGAAAAbWFya2VycRJYEgAAAG1hcmtlcl9jb2x1bW5fbmFtZXETaAJYEwAAAHNhdmVkV2lk
Z2V0R2VvbWV0cnlxFGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoA
AABRQnl0ZUFycmF5cRdDLgHZ0MsAAQAAAAACzAAAAPwAAATIAAADNwAAAtcAAAEpAAAEvQAAAywA
AAAAAABxGIVxGYdxGlJxG1gOAAAAc2V0X2JyZWFrcG9pbnRxHIlYEAAAAHRpbWVzdGFtcF9jb2x1
bW5xHVgEAAAAdGltZXEeWBUAAAB0aW1lc3RhbXBfY29sdW1uX25hbWVxH2gCdS4=
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWBAA
AABkYXRhX3N0cmVhbV9uYW1lcQdYAwAAAGVlZ3EIWA4AAABlbWl0X2VhY2hfdGlja3EJiVgPAAAA
ZXhjbHVkZV9jb2x1bW5zcQpdcQtYCAAAAGZpbGVuYW1lcQxYOwAAAEM6L1VzZXJzL1NpbXJhbi9E
ZXNrdG9wL01TL0JDSS9CQ0lQcm9qL0JDSVByb2ovRGF0YS9zNXAuY3N2cQ1YDwAAAGluY2x1ZGVf
Y29sdW1uc3EOXXEPWBQAAABpbnN0YW5jZV9jb2x1bW5fbmFtZXEQaAJYDQAAAG1hcmtlcl9jb2x1
bW5xEVgGAAAAbWFya2VycRJYEgAAAG1hcmtlcl9jb2x1bW5fbmFtZXETaAJYEwAAAHNhdmVkV2lk
Z2V0R2VvbWV0cnlxFGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoA
AABRQnl0ZUFycmF5cRdDLgHZ0MsAAQAAAAACzAAAAPwAAATIAAADNwAAAtcAAAEpAAAEvQAAAywA
AAAAAABxGIVxGYdxGlJxG1gOAAAAc2V0X2JyZWFrcG9pbnRxHIlYEAAAAHRpbWVzdGFtcF9jb2x1
bW5xHVgEAAAAdGltZXEeWBUAAAB0aW1lc3RhbXBfY29sdW1uX25hbWVxH2gCdS4=
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWBIAAABhY2N1bXVsYXRlX29mZmxpbmVxAYlYCgAAAGNvbmRfZmllbGRxAlgLAAAAVGFy
Z2V0VmFsdWVxA1gNAAAAaWdub3JlX3Jlc2V0c3EEiVgLAAAAbG9zc19tZXRyaWNxBVgDAAAATVNF
cQZYFgAAAG91dHB1dF9mb3Jfc3RhdHNfdGFibGVxB4lYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
CGNzaXAKX3VucGlja2xlX3R5cGUKcQlYDAAAAFB5UXQ0LlF0Q29yZXEKWAoAAABRQnl0ZUFycmF5
cQtDLgHZ0MsAAQAAAAADAgAAAXwAAAR/AAACZwAAAw0AAAGpAAAEdAAAAlwAAAAAAABxDIVxDYdx
DlJxD1gOAAAAc2V0X2JyZWFrcG9pbnRxEIl1Lg==
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAv4AAADnAAAEgwAAAvwAAAMJAAABFAAABHgA
AALxAAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkR0AUAAAAAAAAWAUAAAB0aXRsZXElWBAAAABUaW1lIHNlcmllcyB2aWV3cSZYCgAAAHpl
cm9fY29sb3JxJ1gHAAAAIzdGN0Y3RnEoWAgAAAB6ZXJvbWVhbnEpiHUu
</properties>
		<properties format="literal" node_id="21">{'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWBgAAABhdmVyYWdlX292ZXJfdGltZV93aW5kb3dxAYlYBAAAAGF4aXNxAlgEAAAAdGlt
ZXEDWAcAAABkZXRyZW5kcQRYCAAAAGNvbnN0YW50cQVYCAAAAGZmdF9zaXplcQZYDQAAACh1c2Ug
ZGVmYXVsdClxB1gIAAAAb25lc2lkZWRxCIhYDwAAAG92ZXJsYXBfc2FtcGxlc3EJaAdYEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxCmNzaXAKX3VucGlja2xlX3R5cGUKcQtYDAAAAFB5UXQ0LlF0Q29y
ZXEMWAoAAABRQnl0ZUFycmF5cQ1DLgHZ0MsAAQAAAAADAgAAAXsAAAR/AAACaAAAAw0AAAGoAAAE
dAAAAl0AAAAAAABxDoVxD4dxEFJxEVgHAAAAc2NhbGluZ3ESWAcAAABkZW5zaXR5cRNYDwAAAHNl
Z21lbnRfc2FtcGxlc3EUaAdYDgAAAHNldF9icmVha3BvaW50cRWJWAQAAAB1bml0cRZYBwAAAHNh
bXBsZXNxF1gGAAAAd2luZG93cRhYBAAAAGhhbm5xGXUu
</properties>
		<properties format="literal" node_id="23">{'always_on_top': False, 'antialiased': True, 'autoscale': True, 'background_color': '#FFFFFF', 'decoration_color': '#000000', 'downsampled': False, 'initial_dims': [50, 50, 700, 500], 'line_color': '#000000', 'line_width': 0.75, 'one_over_f_correction': False, 'savedWidgetGeometry': None, 'scale': 1.0, 'set_breakpoint': False, 'stacked': True, 'stream_name': '(use default)', 'title': 'Spectrum view', 'zero_color': '#7F7F7F7F'}</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWBMAAABMb2dpc3RpY1JlZ19jaDEuY3N2cQtYCwAA
AG91dHB1dF9yb290cQxYLgAAAEM6L1VzZXJzL1NpbXJhbi9EZXNrdG9wL01TL0JDSS9CQ0lQcm9q
L0JDSVByb2pxDVgLAAAAcmV0cmlldmFibGVxDolYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2Nz
aXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFycmF5cRJD
LgHZ0MsAAQAAAAADAgAAAS8AAAR/AAACtQAAAw0AAAFcAAAEdAAAAqoAAAAAAABxE4VxFIdxFVJx
FlgOAAAAc2V0X2JyZWFrcG9pbnRxF4lYCwAAAHRpbWVfc3RhbXBzcRiIWA8AAAB0aW1lc3RhbXBf
bGFiZWxxGVgJAAAAdGltZXN0YW1wcRp1Lg==
</properties>
		<properties format="literal" node_id="25">{'cache_size': 200, 'class_weights': '(use default)', 'coef0': [0.0, 1.0], 'cost': [0.01, 0.1, 1.0, 10.0, 100], 'dont_reset_model': False, 'gamma': [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0], 'initialize_once': True, 'kernel': 'rbf', 'max_iter': -1, 'num_folds': 5, 'poly_degree': [1, 2, 3], 'probabilistic': True, 'random_seed': 12345, 'savedWidgetGeometry': None, 'search_metric': 'accuracy', 'set_breakpoint': False, 'shrinking': True, 'tolerance': 0.001, 'verbosity': 0}</properties>
		<properties format="literal" node_id="26">{'class_weights': '(use default)', 'dont_reset_model': False, 'initialize_once': True, 'num_folds': 5, 'probabilistic': True, 'savedWidgetGeometry': None, 'search_metric': 'accuracy', 'set_breakpoint': False, 'shrinkage': [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8], 'verbosity': 0}</properties>
		<properties format="literal" node_id="27">{'class_weights': '(use default)', 'cond_field': 'TargetValue', 'dont_reset_model': False, 'initialize_once': True, 'num_folds': 5, 'probabilistic': True, 'savedWidgetGeometry': None, 'search_metric': 'accuracy', 'set_breakpoint': False, 'shrinkage': 'auto', 'solver': 'eigen', 'tolerance': 0.0001, 'verbosity': 0}</properties>
		<properties format="literal" node_id="28">{'axis_occurrence': 0, 'carry_over_names': True, 'carry_over_numbers': False, 'custom_label': '(use default)', 'init_data': ['low arousal', 'high arousal'], 'new_axis': 'feature', 'old_axis': 'feature', 'only_signals': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="29">{'axis_occurrence': 0, 'carry_over_names': True, 'carry_over_numbers': False, 'custom_label': '(use default)', 'init_data': ['low arousal', 'high arousal'], 'new_axis': 'feature', 'old_axis': 'feature', 'only_signals': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="30">{'axis_occurrence': 0, 'carry_over_names': True, 'carry_over_numbers': False, 'custom_label': '(use default)', 'init_data': ['low arousal', 'high arousal'], 'new_axis': 'feature', 'old_axis': 'feature', 'only_signals': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="literal" node_id="31">{'axis': 'instance', 'force_feature_axis': False, 'ignore_nans': False, 'robust': False, 'robust_estimator_type': 'median', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'trim_proportion': 0.1}</properties>
		<properties format="pickle" node_id="32">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/szMzMzMzNWAwAAABpbml0aWFsX2RpbXNxCV1xCihNIANLMk28Ak30
AWVYDgAAAGluc3RhbmNlX2ZpZWxkcQtYDQAAACh1c2UgZGVmYXVsdClxDFgOAAAAbGFiZWxfcm90
YXRpb25xDVgKAAAAaG9yaXpvbnRhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91
bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDL
AAEAAAAABLMAAAEDAAAGMAAAAsUAAAS+AAABMAAABiUAAAK6AAAAAAAAcROFcRSHcRVScRZYDgAA
AHNldF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRlY
DQAAACh1c2UgZGVmYXVsdClxGlgFAAAAdGl0bGVxG1gRAAAAU1YgQ2xhc3NpZmljYXRpb25xHFgR
AAAAdXNlX2xhc3RfaW5zdGFuY2VxHYhYBwAAAHZlcmJvc2VxHohYCAAAAHlfbGltaXRzcR9dcSAo
SwBLAWV1Lg==
</properties>
		<properties format="literal" node_id="33">{'axis': 'instance', 'force_feature_axis': False, 'ignore_nans': False, 'robust': False, 'robust_estimator_type': 'median', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'trim_proportion': 0.1}</properties>
		<properties format="pickle" node_id="34">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/szMzMzMzNWAwAAABpbml0aWFsX2RpbXNxCV1xCihNIANLMk28Ak30
AWVYDgAAAGluc3RhbmNlX2ZpZWxkcQtYDQAAACh1c2UgZGVmYXVsdClxDFgOAAAAbGFiZWxfcm90
YXRpb25xDVgKAAAAaG9yaXpvbnRhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91
bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDL
AAEAAAAAAwIAAAERAAAEfwAAAtMAAAMNAAABPgAABHQAAALIAAAAAAAAcROFcRSHcRVScRZYDgAA
AHNldF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRlY
DQAAACh1c2UgZGVmYXVsdClxGlgFAAAAdGl0bGVxG1gSAAAATERBIENsYXNzaWZpY2F0aW9ucRxY
EQAAAHVzZV9sYXN0X2luc3RhbmNlcR2IWAcAAAB2ZXJib3NlcR6IWAgAAAB5X2xpbWl0c3EfXXEg
KEsASwFldS4=
</properties>
		<properties format="literal" node_id="35">{'axis': 'instance', 'force_feature_axis': False, 'ignore_nans': False, 'robust': False, 'robust_estimator_type': 'median', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'trim_proportion': 0.1}</properties>
		<properties format="pickle" node_id="36">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/szMzMzMzNWAwAAABpbml0aWFsX2RpbXNxCV1xCihNIANLMk28Ak30
AWVYDgAAAGluc3RhbmNlX2ZpZWxkcQtYDQAAACh1c2UgZGVmYXVsdClxDFgOAAAAbGFiZWxfcm90
YXRpb25xDVgKAAAAaG9yaXpvbnRhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91
bnBpY2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDL
AAEAAAAAAwIAAAERAAAEfwAAAtMAAAMNAAABPgAABHQAAALIAAAAAAAAcROFcRSHcRVScRZYDgAA
AHNldF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRlY
DQAAACh1c2UgZGVmYXVsdClxGlgFAAAAdGl0bGVxG1gSAAAAUURBIENsYXNzaWZpY2F0aW9ucRxY
EQAAAHVzZV9sYXN0X2luc3RhbmNlcR2IWAcAAAB2ZXJib3NlcR6IWAgAAAB5X2xpbWl0c3EfXXEg
KEsASwFldS4=
</properties>
		<properties format="pickle" node_id="37">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWAoAAABTVl9jaDEuY3N2cQtYCwAAAG91dHB1dF9y
b290cQxYLgAAAEM6L1VzZXJzL1NpbXJhbi9EZXNrdG9wL01TL0JDSS9CQ0lQcm9qL0JDSVByb2px
DVgLAAAAcmV0cmlldmFibGVxDolYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxD2NzaXAKX3VucGlj
a2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABRQnl0ZUFycmF5cRJDLgHZ0MsAAQAA
AAADAgAAAS8AAAR/AAACtQAAAw0AAAFcAAAEdAAAAqoAAAAAAABxE4VxFIdxFVJxFlgOAAAAc2V0
X2JyZWFrcG9pbnRxF4lYCwAAAHRpbWVfc3RhbXBzcRiIWA8AAAB0aW1lc3RhbXBfbGFiZWxxGVgJ
AAAAdGltZXN0YW1wcRp1Lg==
</properties>
		<properties format="pickle" node_id="38">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWAsAAABMREFfY2gxLmNzdnELWAsAAABvdXRwdXRf
cm9vdHEMWC4AAABDOi9Vc2Vycy9TaW1yYW4vRGVza3RvcC9NUy9CQ0kvQkNJUHJvai9CQ0lQcm9q
cQ1YCwAAAHJldHJpZXZhYmxlcQ6JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBp
Y2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEA
AAAAAwIAAAEvAAAEfwAAArUAAAMNAAABXAAABHQAAAKqAAAAAAAAcROFcRSHcRVScRZYDgAAAHNl
dF9icmVha3BvaW50cReJWAsAAAB0aW1lX3N0YW1wc3EYiFgPAAAAdGltZXN0YW1wX2xhYmVscRlY
CQAAAHRpbWVzdGFtcHEadS4=
</properties>
		<properties format="pickle" node_id="39">gAN9cQAoWBcAAABhYnNvbHV0ZV9pbnN0YW5jZV90aW1lc3EBiFgNAAAAY2xvdWRfYWNjb3VudHEC
WAAAAABxA1gMAAAAY2xvdWRfYnVja2V0cQRoA1gRAAAAY2xvdWRfY3JlZGVudGlhbHNxBWgDWAoA
AABjbG91ZF9ob3N0cQZYBwAAAERlZmF1bHRxB1gNAAAAY29sdW1uX2hlYWRlcnEIiFgMAAAAZGVs
ZXRlX3BhcnRzcQmIWAgAAABmaWxlbmFtZXEKWAsAAABRREFfY2gxLmNzdnELWAsAAABvdXRwdXRf
cm9vdHEMWC4AAABDOi9Vc2Vycy9TaW1yYW4vRGVza3RvcC9NUy9CQ0kvQkNJUHJvai9CQ0lQcm9q
cQ1YCwAAAHJldHJpZXZhYmxlcQ6JWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBp
Y2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEA
AAAAAwIAAAEvAAAEfwAAArUAAAMNAAABXAAABHQAAAKqAAAAAAAAcROFcRSHcRVScRZYDgAAAHNl
dF9icmVha3BvaW50cReJWAsAAAB0aW1lX3N0YW1wc3EYiFgPAAAAdGltZXN0YW1wX2xhYmVscRlY
CQAAAHRpbWVzdGFtcHEadS4=
</properties>
		<properties format="literal" node_id="40">{'chunk_len': 0, 'ignore_signal_changed': False, 'marker_name': 'OutStream-markers', 'marker_source_id': '', 'max_buffered': 60, 'reset_if_labels_changed': False, 'savedWidgetGeometry': None, 'send_markers': False, 'set_breakpoint': False, 'source_id': '(never use same source id in one pypeline)', 'srate': '(use default)', 'stream_name': 'OutStream', 'stream_type': 'Control', 'use_data_timestamps': True, 'use_numpy_optimization': False}</properties>
		<properties format="literal" node_id="41">{'chunk_len': 0, 'ignore_signal_changed': False, 'marker_name': 'OutStream-markers', 'marker_source_id': '', 'max_buffered': 60, 'reset_if_labels_changed': False, 'savedWidgetGeometry': None, 'send_markers': False, 'set_breakpoint': False, 'source_id': '(never use same source id in one pypeline)', 'srate': '(use default)', 'stream_name': 'OutStream', 'stream_type': 'Control', 'use_data_timestamps': True, 'use_numpy_optimization': False}</properties>
		<properties format="literal" node_id="42">{'chunk_len': 0, 'ignore_signal_changed': False, 'marker_name': 'OutStream-markers', 'marker_source_id': '', 'max_buffered': 60, 'reset_if_labels_changed': False, 'savedWidgetGeometry': None, 'send_markers': False, 'set_breakpoint': False, 'source_id': '(never use same source id in one pypeline)', 'srate': '(use default)', 'stream_name': 'OutStream', 'stream_type': 'Control', 'use_data_timestamps': True, 'use_numpy_optimization': False}</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node3",
            "data",
            "node6",
            "data"
        ],
        [
            "node6",
            "data",
            "node4",
            "data"
        ],
        [
            "node6",
            "data",
            "node26",
            "data"
        ],
        [
            "node6",
            "data",
            "node28",
            "data"
        ],
        [
            "node6",
            "data",
            "node27",
            "data"
        ],
        [
            "node5",
            "data",
            "node8",
            "data"
        ],
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node8",
            "data",
            "node1",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "streaming_data"
        ],
        [
            "node9",
            "data",
            "node5",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "data"
        ],
        [
            "node12",
            "data",
            "node7",
            "data"
        ],
        [
            "node4",
            "data",
            "node13",
            "data"
        ],
        [
            "node4",
            "data",
            "node16",
            "data"
        ],
        [
            "node4",
            "data",
            "node25",
            "data"
        ],
        [
            "node16",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node15",
            "data"
        ],
        [
            "node18",
            "data",
            "node10",
            "data"
        ],
        [
            "node19",
            "data",
            "node9",
            "calib_data"
        ],
        [
            "node23",
            "data",
            "node24",
            "data"
        ],
        [
            "node2",
            "data",
            "node23",
            "data"
        ],
        [
            "node2",
            "data",
            "node21",
            "data"
        ],
        [
            "node2",
            "data",
            "node14",
            "data"
        ],
        [
            "node20",
            "loss",
            "node22",
            "data"
        ],
        [
            "node14",
            "data",
            "node3",
            "data"
        ],
        [
            "node26",
            "data",
            "node31",
            "data"
        ],
        [
            "node26",
            "data",
            "node38",
            "data"
        ],
        [
            "node26",
            "data",
            "node41",
            "data"
        ],
        [
            "node28",
            "data",
            "node30",
            "data"
        ],
        [
            "node28",
            "data",
            "node39",
            "data"
        ],
        [
            "node28",
            "data",
            "node42",
            "data"
        ],
        [
            "node28",
            "data",
            "node20",
            "data"
        ],
        [
            "node27",
            "data",
            "node29",
            "data"
        ],
        [
            "node27",
            "data",
            "node40",
            "data"
        ],
        [
            "node27",
            "data",
            "node43",
            "data"
        ],
        [
            "node32",
            "data",
            "node33",
            "data"
        ],
        [
            "node34",
            "data",
            "node35",
            "data"
        ],
        [
            "node36",
            "data",
            "node37",
            "data"
        ],
        [
            "node31",
            "data",
            "node32",
            "data"
        ],
        [
            "node30",
            "data",
            "node34",
            "data"
        ],
        [
            "node29",
            "data",
            "node36",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        2.0,
                        4.0,
                        42.0,
                        45.0
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "e74911dd-3f6d-4071-8dea-aa873888dedf"
        },
        "node10": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "looping": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 100
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "deterministic"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "17f9f59a-09c3-4813-80e7-79c600b3f682"
        },
        "node11": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "OutStreamData-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "mysourceid234"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "OutStreamData"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0e2ea86a-0758-4f2b-8713-b91d68a7f1f9"
        },
        "node12": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='OutStreamData-markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='OutStreamData'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "fb1e3721-795e-48cc-b108-5e792b869355"
        },
        "node13": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "bbbdabce-9154-46a8-adb6-83a199287ab6"
        },
        "node14": {
            "class": "FilterBankCommonSpatialPattern",
            "module": "neuropype.nodes.neural.FilterBankCommonSpatialPattern",
            "params": {
                "bands": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        [
                            4,
                            7
                        ],
                        [
                            8,
                            12
                        ],
                        [
                            13,
                            30
                        ],
                        [
                            31,
                            42
                        ]
                    ]
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "min_fft_size": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 512
                },
                "nof": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "overlap_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "overlap_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "window_func": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "hann"
                },
                "window_length": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "window_param": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "window_unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                }
            },
            "uuid": "2aeb11da-cd22-458e-bdfc-fbffd8ec6735"
        },
        "node15": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Logistic Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "06d617cd-460b-4a84-9b89-fdab04d9dfa3"
        },
        "node16": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "low arousal",
                        "high arousal"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a0335d71-e54b-4aac-9540-20feb1738039"
        },
        "node17": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "32cc0e60-a4a9-4ac7-8b74-38c0303fb367"
        },
        "node18": {
            "class": "ImportCSV",
            "module": "neuropype.nodes.file_system.ImportCSV",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "data_stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "emit_each_tick": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj/Data/s32.csv"
                },
                "include_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "instance_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "marker_column": {
                    "customized": true,
                    "type": "Port",
                    "value": "marker"
                },
                "marker_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "timestamp_column": {
                    "customized": true,
                    "type": "Port",
                    "value": "time"
                },
                "timestamp_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                }
            },
            "uuid": "7f652bfb-9339-405e-ad14-4aec2ff732a0"
        },
        "node19": {
            "class": "ImportCSV",
            "module": "neuropype.nodes.file_system.ImportCSV",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "data_stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "eeg"
                },
                "emit_each_tick": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "exclude_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj/Data/s5p.csv"
                },
                "include_columns": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "instance_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "marker_column": {
                    "customized": true,
                    "type": "Port",
                    "value": "marker"
                },
                "marker_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "timestamp_column": {
                    "customized": true,
                    "type": "Port",
                    "value": "time"
                },
                "timestamp_column_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                }
            },
            "uuid": "3cf1f3e9-1415-4102-a563-8fbd7b79fe66"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        5
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "6fd7ccba-3998-4f33-87f3-6994253234a1"
        },
        "node20": {
            "class": "MeasureLoss",
            "module": "neuropype.nodes.machine_learning.MeasureLoss",
            "params": {
                "accumulate_offline": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "ignore_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "loss_metric": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "MSE"
                },
                "output_for_stats_table": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "685cd964-e1ba-4e81-ac26-9fd759d9bfec"
        },
        "node21": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "2e589c55-86b4-46a4-bd04-c38901a91517"
        },
        "node22": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "4de354a5-9959-4858-a100-58037d8c0780"
        },
        "node23": {
            "class": "WelchSpectrum",
            "module": "neuropype.nodes.spectral.WelchSpectrum",
            "params": {
                "average_over_time_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "detrend": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "constant"
                },
                "fft_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "onesided": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "overlap_samples": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "scaling": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "density"
                },
                "segment_samples": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "samples"
                },
                "window": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "hann"
                }
            },
            "uuid": "07ad03ba-8b33-4d43-b470-4b13b6ef77f3"
        },
        "node24": {
            "class": "SpectrumPlot",
            "module": "neuropype.nodes.visualization.SpectrumPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "one_over_f_correction": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stacked": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Spectrum view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F7F"
                }
            },
            "uuid": "ab336258-99d8-41b7-af98-3e54499b41b5"
        },
        "node25": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "LogisticReg_ch1.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "e89f1352-58cf-43e4-bfb7-b490a32227d2"
        },
        "node26": {
            "class": "SupportVectorClassification",
            "module": "neuropype.nodes.machine_learning.SupportVectorClassification",
            "params": {
                "cache_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 200
                },
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "coef0": {
                    "customized": false,
                    "type": "Port",
                    "value": [
                        0.0,
                        1.0
                    ]
                },
                "cost": {
                    "customized": false,
                    "type": "Port",
                    "value": [
                        0.01,
                        0.1,
                        1.0,
                        10.0,
                        100
                    ]
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "gamma": {
                    "customized": false,
                    "type": "Port",
                    "value": [
                        0.0001,
                        0.001,
                        0.01,
                        0.1,
                        1.0,
                        10.0
                    ]
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "kernel": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "rbf"
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "poly_degree": {
                    "customized": false,
                    "type": "Port",
                    "value": [
                        1,
                        2,
                        3
                    ]
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "random_seed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 12345
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinking": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "43ac7ab1-bd6b-49ee-8a88-3332b22479de"
        },
        "node27": {
            "class": "QuadraticDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.QuadraticDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0,
                        0.1,
                        0.2,
                        0.3,
                        0.4,
                        0.5,
                        0.6,
                        0.8
                    ]
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "a4a0981e-b187-4e0b-85b1-d7f244ffbb9b"
        },
        "node28": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "ae5098f8-4671-4bb1-bddf-cfc3b4cfcdd2"
        },
        "node29": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "low arousal",
                        "high arousal"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "11b7798c-fafd-471c-87c1-96058c8e7b6d"
        },
        "node3": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "02f46fbf-dc00-4a39-b18a-4e78c2683608"
        },
        "node30": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "low arousal",
                        "high arousal"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "abf345bc-38bf-424e-a031-dbe9ae589cd1"
        },
        "node31": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "low arousal",
                        "high arousal"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c0e02d83-9728-4fb0-8bb3-d36e429570b3"
        },
        "node32": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "835839c5-8ab6-4b88-938a-bfcca5e5596a"
        },
        "node33": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "SV Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "61210659-96f4-48e4-9441-04a56860bb33"
        },
        "node34": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "b79581fa-1e80-47b9-95c7-2cf9bda02717"
        },
        "node35": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "LDA Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "f850c0e6-f79f-4ebd-812d-096894be9d67"
        },
        "node36": {
            "class": "Mean",
            "module": "neuropype.nodes.statistics.Mean",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "instance"
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "robust_estimator_type": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "median"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "trim_proportion": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                }
            },
            "uuid": "f4568184-28fa-4c2f-8b0a-892d4e160896"
        },
        "node37": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 0.9
                },
                "initial_dims": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        800,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "horizontal"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "QDA Classification"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "fde57fa6-d83d-4040-94c5-3f040785d798"
        },
        "node38": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "SV_ch1.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "8864f9dc-81da-4efd-8763-acf5fdcd6256"
        },
        "node39": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "LDA_ch1.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "407ba5a0-ebd6-4107-b2eb-8ebd0508e8f2"
        },
        "node4": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "e7c7692f-b21c-4755-8015-ffa322d52a5e"
        },
        "node40": {
            "class": "RecordToCSV",
            "module": "neuropype.nodes.file_system.RecordToCSV",
            "params": {
                "absolute_instance_times": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "column_header": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "QDA_ch1.csv"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "C:/Users/Simran/Desktop/MS/BCI/BCIProj/BCIProj"
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_stamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "timestamp_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "timestamp"
                }
            },
            "uuid": "3e0e2b2a-0256-4d74-83c8-2aa293f1c787"
        },
        "node41": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "4055b631-0d38-4a7e-8d41-6413bce87aef"
        },
        "node42": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e158d816-35b6-4376-9e4c-3d06896f7ed9"
        },
        "node43": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(never use same source id in one pypeline)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "24488188-1c06-425a-a6ca-47706f574d82"
        },
        "node5": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "high": 1,
                        "low": 0
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "37d61b72-2810-4e5e-8c2c-a9e00f67f954"
        },
        "node6": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "fe52b38a-25d1-4407-a062-2acbd0d54cd2"
        },
        "node7": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 300
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "2b52573f-2f7e-4cfa-9316-2f3d4f15bd2f"
        },
        "node8": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": ":-1"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "1d3a3fcf-a089-4009-a465-ae787997c410"
        },
        "node9": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2a90fa36-aff8-480d-aaa4-8d0f71ba25d9"
        }
    },
    "version": 1.1
}</patch>
</scheme>
