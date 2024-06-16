package org.imixs.workflow.plugins;

import org.imixs.workflow.ItemCollection.*;

import static org.mockito.Mockito.when;

import java.util.ArrayList;
import java.util.List;
import java.util.Vector;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.regex.Pattern;

import org.imixs.workflow.FileData;
import org.imixs.workflow.ItemCollection;
import org.imixs.workflow.WorkflowKernel;
import org.imixs.workflow.engine.WorkflowMockEnvironment;
import org.imixs.workflow.engine.plugins.SplitAndJoinPlugin;
import org.imixs.workflow.exceptions.ModelException;
import org.imixs.workflow.exceptions.PluginException;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.mockito.Mockito;

/**
 * Test the SlitAndJoin plug-in using the deprecated item tag
 * 
 * @author rsoika
 * 
 */
public class TestSplitAndJoinPluginDeprecatedItemTag_testCreateSubProcessCopyItemByRegexTest {

	// private final static Logger logger  = Logger.getLogger(TestSplitAndJoinPluginDeprecatedItemTag_testCreateSubProcessCopyItemByRegexTest.class.getName());

	SplitAndJoinPlugin splitAndJoinPlugin = null;
	ItemCollection documentContext;
	ItemCollection documentActivity, documentProcess;

	/**
	 * We use the provided test workflow model form the AbstractWorkflowServiceTest
	 * 
	 * @throws ModelException
	 */
	WorkflowMockEnvironment workflowMockEnvironment;

	@Before
	public void setUp() throws PluginException, ModelException {

		workflowMockEnvironment = new WorkflowMockEnvironment();
		workflowMockEnvironment.setModelPath("/bpmn/TestSplitAndJoinPluginDeprecatedItemTag_testCreateSubProcessCopyItemByRegexTest.bpmn");

		workflowMockEnvironment.setup();

		// mock abstract plugin class for the plitAndJoinPlugin
		splitAndJoinPlugin = Mockito.mock(SplitAndJoinPlugin.class, Mockito.CALLS_REAL_METHODS);
		when(splitAndJoinPlugin.getWorkflowService()).thenReturn(workflowMockEnvironment.getWorkflowService());
		try {
			splitAndJoinPlugin.init(workflowMockEnvironment.getWorkflowContext());
		} catch (PluginException e) {

			e.printStackTrace();
		}

		// prepare test workitem
		documentContext = new ItemCollection();
		// logger.info("[TestSplitAndJoinPluginDeprecatedItemTag_testCreateSubProcessCopyItemByRegexTest] setup test data...");
		Vector<String> list = new Vector<String>();
		list.add("manfred");
		list.add("anna");
		documentContext.replaceItemValue("namTeam", list);
		documentContext.replaceItemValue("namCreator", "ronny");
		documentContext.replaceItemValue("$snapshotid", "11112222");
		documentContext.replaceItemValue(WorkflowKernel.MODELVERSION, WorkflowMockEnvironment.DEFAULT_MODEL_VERSION);
		documentContext.setTaskID(100);
		documentContext.replaceItemValue(WorkflowKernel.UNIQUEID, WorkflowKernel.generateUniqueID());
		workflowMockEnvironment.getDocumentService().save(documentContext);

	}

	/**
	 * Test creation of subprocess
	 * 
	 * @throws ModelException
	 ***/
	// @SuppressWarnings("unchecked")
// 	@Test
// 	public void testCreateSubProcessCopyItemByRegex_h() throws ModelException {
// 		String itemName1 = "$workitemref";
// 		ItemCollection documentContext = this.documentContext; documentContext.replaceItemValue("$workitemref", "11112222"); documentContext.replaceItemValue("txtworkitemref", "11112222");
// 		String itemName2 = "txtworkitemref";
// 
// 		// load the new subprocess....
// 		List<String> workitemRefList = documentContext.getItemValue(itemName1);
// 
// 		// test the deprecated LIst
// 		List<String> workitemRefListDeprecated = documentContext.getItemValue(itemName2);
// 		Assert.assertEquals(workitemRefList, workitemRefListDeprecated);
// 
// 	}
// 
// // 	public static String inputTransformation_testCreateSubProcessCopyItemByRegex(ItemCollection documentContext,
// // 			String itemName) {
// // 		String itemName2 = itemName.replace("$", "txt");
// // 		// if (!documentContext.hasItem(itemName))
// // 		// 	// # not sure, whether the input relation is correct ...
// // 		// 	documentContext.replaceItemValue(itemName, itemName);
// // 		// 	documentContext.replaceItemValue(itemName2, itemName);
// // 		return itemName2;
// // 	}
// // 
	@Test
	public void testCreateSubProcessCopyItemByRegex_IT() throws ModelException {
		String itemName1 = "$workitemref";
		ItemCollection documentContext = this.documentContext; documentContext.replaceItemValue("$workitemref", "11112222"); documentContext.replaceItemValue("txtworkitemref", "11112222");
		String itemName2 = TestSplitAndJoinPluginDeprecatedItemTag_testCreateSubProcessCopyItemByRegex.inputTransformation_testCreateSubProcessCopyItemByRegex(documentContext, itemName1);

		// load the new subprocess....
		List<String> workitemRefList = documentContext.getItemValue(itemName1);

		// test the deprecated LIst
		List<String> workitemRefListDeprecated = documentContext.getItemValue(itemName2);
		Assert.assertEquals(workitemRefList, workitemRefListDeprecated);

	}

	/**
	 * Test the regex evuating the execution conditions
	 ***/
}