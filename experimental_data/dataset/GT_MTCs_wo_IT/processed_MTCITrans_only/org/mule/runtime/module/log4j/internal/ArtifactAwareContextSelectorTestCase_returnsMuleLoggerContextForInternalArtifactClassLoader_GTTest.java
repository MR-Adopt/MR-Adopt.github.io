/*
 * Copyright 2023 Salesforce, Inc. All rights reserved.
 * The software in this package is published under the terms of the CPAL v1.0
 * license, a copy of which has been included with this distribution in the
 * LICENSE.txt file.
 */
package org.mule.runtime.module.log4j.internal;

import org.mule.runtime.module.log4j.internal.ArtifactAwareContextSelector;
import org.mule.runtime.module.log4j.internal.ArtifactAwareContextSelector.*;

import static org.mule.runtime.api.util.MuleSystemProperties.MULE_LOG_CONTEXT_DISPOSE_DELAY_MILLIS;
import static org.mule.runtime.core.internal.util.MuleContainerUtils.getMuleHome;
import static org.mule.runtime.module.log4j.internal.LoggerContextReaperThreadFactory.THREAD_NAME;
import static org.mule.runtime.module.log4j.internal.MuleLoggerContextFactory.LOG4J_CONFIGURATION_FILE_PROPERTY;
import static org.mule.tck.MuleTestUtils.getRunningThreadByName;

import static org.apache.commons.lang3.StringUtils.EMPTY;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.notNullValue;
import static org.hamcrest.CoreMatchers.sameInstance;
import static org.hamcrest.core.IsInstanceOf.instanceOf;
import static org.hamcrest.core.IsNot.not;
import static org.junit.Assert.assertThat;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.RETURNS_MOCKS;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.mule.runtime.api.util.Reference;
import org.mule.runtime.deployment.model.api.application.ApplicationDescriptor;
import org.mule.runtime.deployment.model.api.policy.PolicyTemplateDescriptor;
import org.mule.runtime.module.artifact.api.classloader.ArtifactClassLoader;
import org.mule.runtime.module.artifact.api.classloader.ClassLoaderLookupPolicy;
import org.mule.runtime.module.artifact.api.classloader.MuleArtifactClassLoader;
import org.mule.runtime.module.artifact.api.classloader.RegionClassLoader;
import org.mule.runtime.module.artifact.api.classloader.ShutdownListener;
import org.mule.runtime.module.artifact.api.descriptor.DeployableArtifactDescriptor;
import org.mule.tck.junit4.AbstractMuleTestCase;
import org.mule.tck.junit4.rule.SystemProperty;
import org.mule.tck.probe.JUnitProbe;
import org.mule.tck.probe.PollingProber;
import org.mule.tck.probe.Probe;
import org.mule.tck.size.SmallTest;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.List;
import java.util.Arrays;

import org.apache.logging.log4j.core.LifeCycle;
import org.apache.logging.log4j.core.LoggerContext;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;

import org.mockito.Answers;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnit;
import org.mockito.junit.MockitoRule;

@SmallTest
public class ArtifactAwareContextSelectorTestCase_returnsMuleLoggerContextForInternalArtifactClassLoader_GTTest extends AbstractMuleTestCase {

  private static final String POLICY_TEMPLATE_NAME = "policyTemplate";
  private static final String POLICY_TEMPLATE_ARTIFACT_ID = "domain/app/anApp/policy/aPolicy";

  private static final File CONFIG_LOCATION = new File("src/test/resources/log4j2-test-custom.xml");
  private static final int PROBER_TIMEOUT = 5000;
  private static final int PROBER_FREQ = 500;

  @Rule
  public MockitoRule rule = MockitoJUnit.rule().silent();

  @Rule
  public SystemProperty disposeDelay = new SystemProperty(MULE_LOG_CONTEXT_DISPOSE_DELAY_MILLIS, "200");

  @Rule
  public SystemProperty log4jConfigurationFile = new SystemProperty("log4j.configurationFile", null);

  private ArtifactAwareContextSelector selector;

  @Mock(answer = Answers.RETURNS_DEEP_STUBS)
  private RegionClassLoader regionClassLoader;

  @Mock
  private DeployableArtifactDescriptor deployableArtifactDescriptor;

  @Before
  public void before() throws Exception {
    selector = new ArtifactAwareContextSelector();

    when(regionClassLoader.getArtifactId()).thenReturn(getClass().getName());
    when(regionClassLoader.findLocalResource("log4j2.xml")).thenReturn(CONFIG_LOCATION.toURI().toURL());
    when(regionClassLoader.findLocalResource("log4j2-test.xml")).thenReturn(CONFIG_LOCATION.toURI().toURL());
    when(regionClassLoader.getArtifactDescriptor()).thenReturn(deployableArtifactDescriptor);
  }

  // @After
  // public void after() throws Exception {
  //   dispose();
  // }

//   @Test
//   public void returnsMuleLoggerContextForInternalArtifactClassLoader_h() {
//     String fqcn = "";
//     boolean currentContext = true;
//     ClassLoader systemLoader = this.getClass().getClassLoader();
// 
//     String fqcn2 = "";
//     boolean currentContext2 = true;
//     
//     ArtifactClassLoader serviceClassLoader =
//         new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(),
//                                     mock(ClassLoaderLookupPolicy.class));
//     ClassLoader serviceLoader = serviceClassLoader.getClassLoader();        
//                       
//     LoggerContext systemContext = selector.getContext(fqcn, systemLoader, currentContext);
//     LoggerContext serviceCtx = selector.getContext(fqcn2, serviceLoader, currentContext2);
//     assertThat(serviceCtx, instanceOf(MuleLoggerContext.class));
//     assertThat(serviceCtx, sameInstance(systemContext));
//   }
// 
// //   public static List<Object> inputTransformation_returnsMuleLoggerContextForInternalArtifactClassLoader(String fqcn, boolean currentContext, ClassLoader systemLoader) {
// // 		String fqcn2 = fqcn;
// //     boolean currentContext2 = currentContext;
// //     // ClassLoader serviceLoader = new URLClassLoader(new URL[0], systemLoader);
// //     ClassLoader serviceLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], systemLoader, mock(ClassLoaderLookupPolicy.class));
// // 		List<Object> transformed_inputs = Arrays.asList(fqcn, serviceLoader,currentContext2);
// // 		return transformed_inputs;
// // 	}
// // 
  @Test
  public void returnsMuleLoggerContextForInternalArtifactClassLoader_IT() {
    String fqcn = "";
    boolean currentContext = true;
    ClassLoader systemLoader =this.getClass().getClassLoader();

    List<Object> transformed_inputs = ArtifactAwareContextSelectorTestCase_returnsMuleLoggerContextForInternalArtifactClassLoader_GT.inputTransformation_returnsMuleLoggerContextForInternalArtifactClassLoader(fqcn, currentContext, systemLoader);
    String fqcn2 = (String) transformed_inputs.get(0);
    boolean currentContext2 = (boolean) transformed_inputs.get(2);
    ClassLoader serviceLoader = (ClassLoader) transformed_inputs.get(1);
                      
    LoggerContext systemContext = selector.getContext(fqcn, systemLoader, currentContext);
    LoggerContext serviceCtx = selector.getContext(fqcn2, serviceLoader, currentContext2);
    assertThat(serviceCtx, instanceOf(MuleLoggerContext.class));
    assertThat(serviceCtx, sameInstance(systemContext));
  }

  private void assertReaperThreadNotRunning() {
    PollingProber prober = new PollingProber(PROBER_TIMEOUT, PROBER_FREQ);
    prober.check(new Probe() {

      @Override
      public boolean isSatisfied() {
        return getReaperThread() == null;
      }

      @Override
      public String describeFailure() {
        return "Reaper thread exists from previous test and did not died";
      }
    });
  }

  private Thread getReaperThread() {
    return getRunningThreadByName(THREAD_NAME);
  }

  private MuleLoggerContext getContext() {
    return (MuleLoggerContext) selector.getContext("", regionClassLoader, true);
  }

  private void assertConfigurationLocation(LoggerContext ctx) {
    assertThat(ctx.getConfigLocation(), equalTo(CONFIG_LOCATION.toURI()));
  }

  private RegionClassLoader getPolicyRegionClassLoader(PolicyTemplateDescriptor policyTemplateDescriptor) {
    return new RegionClassLoader(POLICY_TEMPLATE_ARTIFACT_ID, policyTemplateDescriptor, regionClassLoader,
                                 mock(ClassLoaderLookupPolicy.class));
  }

  private MuleArtifactClassLoader getPolicyArtifactClassLoader(PolicyTemplateDescriptor policyTemplateDescriptor,
                                                               RegionClassLoader policyRegionClassLoader) {
    return new MuleArtifactClassLoader(POLICY_TEMPLATE_ARTIFACT_ID, policyTemplateDescriptor, new URL[0], policyRegionClassLoader,
                                       mock(ClassLoaderLookupPolicy.class));
  }

  private void assertStopped(final MuleLoggerContext context) {
    final Reference<Boolean> contextWasAccessibleDuringShutdown = new Reference<>(true);
    PollingProber pollingProber = new PollingProber(1000, 10);
    pollingProber.check(new JUnitProbe() {

      @Override
      protected boolean test() throws Exception {
        if (context.getState().equals(LifeCycle.State.STOPPED)) {
          assertThat(context, not(getContext()));
          return true;
        } else {
          LoggerContext currentContext = getContext();
          if (currentContext != null && currentContext != context) {
            contextWasAccessibleDuringShutdown.set(false);
          }
          return false;
        }
      }

      @Override
      public String describeFailure() {
        return "context was not stopped";
      }
    });

    assertThat(contextWasAccessibleDuringShutdown.get(), is(true));
  }
}