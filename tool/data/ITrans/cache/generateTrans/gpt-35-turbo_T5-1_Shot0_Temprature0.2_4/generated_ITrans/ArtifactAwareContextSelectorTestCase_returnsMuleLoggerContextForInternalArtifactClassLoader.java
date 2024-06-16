package org.mule.runtime.module.log4j.internal;

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


import org.mule.runtime.module.log4j.internal.ArtifactAwareContextSelector;
import org.mule.runtime.module.log4j.internal.ArtifactAwareContextSelector.*;
import java.util.List;
import java.util.Arrays;

public class ArtifactAwareContextSelectorTestCase_returnsMuleLoggerContextForInternalArtifactClassLoader {
    public static List<Object> inputTransformation_returnsMuleLoggerContextForInternalArtifactClassLoader(String fqcn, boolean currentContext, ClassLoader systemLoader)  {
        String fqcn2 = fqcn;
        ClassLoader serviceLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], systemLoader, mock(ClassLoaderLookupPolicy.class)).getClassLoader();
        boolean currentContext2 = currentContext;
        List<Object> transformed_inputs = Arrays.asList(fqcn2, serviceLoader, currentContext2);
        return transformed_inputs;
    }
}