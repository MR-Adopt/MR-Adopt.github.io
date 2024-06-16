/*
 * Copyright 2023 Salesforce, Inc. All rights reserved.
 * The software in this package is published under the terms of the CPAL v1.0
 * license, a copy of which has been included with this distribution in the
 * LICENSE.txt file.
 */
package org.mule.runtime.module.deployment.test.internal.singleapp;

import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDeploymentService.*;
import static org.mule.test.allure.AllureConstants.ArtifactDeploymentFeature.APP_DEPLOYMENT;
import static org.mule.test.allure.AllureConstants.ArtifactDeploymentFeature.SingleAppDeploymentStory.SINGLE_APP_DEPLOYMENT;
import static java.net.URI.create;
import static org.hamcrest.Matchers.hasItems;
import static org.junit.Assert.assertThat;
import static org.junit.rules.ExpectedException.none;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import org.mule.runtime.api.scheduler.SchedulerService;
import org.mule.runtime.deployment.model.api.application.Application;
import org.mule.runtime.deployment.model.api.domain.Domain;
import org.mule.runtime.module.deployment.api.DeploymentListener;
import org.mule.runtime.module.deployment.api.StartupListener;
import org.mule.runtime.module.deployment.internal.DefaultArchiveDeployer;
import org.mule.runtime.module.deployment.internal.DeploymentFileResolver;
import org.mule.runtime.module.deployment.internal.DomainArchiveDeployer;
import org.mule.runtime.module.deployment.internal.singleapp.SingleAppApplicationDeployerBuilder;
import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDeploymentService;
import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDomainDeployerBuilder;
import org.mule.tck.junit4.AbstractMuleTestCase;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;
import java.util.function.Consumer;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;

@Feature(APP_DEPLOYMENT)
@Story(SINGLE_APP_DEPLOYMENT)
public class SingleAppDeploymentServiceTestCase_startupListeners_h6Test3 extends AbstractMuleTestCase {

    public static final URI ARCHIVE_URI = create("");

    private static final String APP = "APP";

    public static final String DOMAIN = "DOMAIN";

    @Rule
    public ExpectedException expectedException = none();

    private static SingleAppDeploymentService getSingleAppDeploymentService() {
        DomainArchiveDeployer appDomainDeployer = mock(DomainArchiveDeployer.class);
        SingleAppDomainDeployerBuilder singleAppDomainDeployerBuilder = mockSingleAppDomainDeployerBuilder(appDomainDeployer);
        SingleAppApplicationDeployerBuilder singleAppApplicationDeployerBuilder = mockSingleAppApplicationDeployerBuilder();
        DefaultArchiveDeployer archiveDeployer = mock(DefaultArchiveDeployer.class);
        when(singleAppApplicationDeployerBuilder.build()).thenReturn(archiveDeployer);
        List<Domain> domains = new ArrayList<>();
        List<Application> applications = new ArrayList<>();
        Application application = mock(Application.class);
        applications.add(application);
        DeploymentFileResolver fileResolver = mock(DeploymentFileResolver.class);
        SchedulerService schedulerService = mock(SchedulerService.class);
        SingleAppDeploymentService singleAppDeploymentService = new SingleAppDeploymentService(singleAppDomainDeployerBuilder, singleAppApplicationDeployerBuilder, fileResolver, applications, domains, () -> schedulerService);
        return singleAppDeploymentService;
    }

    @Test
    public void startupListeners_h6Test3() {
        SingleAppDeploymentService singleAppDeploymentService = getSingleAppDeploymentService();
    StartupListener startUpListener1 = new StartupListener() {
        @Override
        public void onStartup() {
            // Implementation that does nothing
        }
        singleAppDeploymentService.addStartupListener(startUpListener1);
        singleAppDeploymentService.addStartupListener(startUpListener2);
        assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
    }

    private static SingleAppApplicationDeployerBuilder mockSingleAppApplicationDeployerBuilder() {
        SingleAppApplicationDeployerBuilder singleAppApplicationDeployerBuilder = mock(SingleAppApplicationDeployerBuilder.class);
        when(singleAppApplicationDeployerBuilder.withApplicationDeployer(any())).thenReturn(singleAppApplicationDeployerBuilder);
        when(singleAppApplicationDeployerBuilder.withApplicationDeploymentListener(any())).thenReturn(singleAppApplicationDeployerBuilder);
        when(singleAppApplicationDeployerBuilder.withApplications(any())).thenReturn(singleAppApplicationDeployerBuilder);
        when(singleAppApplicationDeployerBuilder.withApplicationFactory(any())).thenReturn(singleAppApplicationDeployerBuilder);
        return singleAppApplicationDeployerBuilder;
    }

    private static SingleAppDomainDeployerBuilder mockSingleAppDomainDeployerBuilder(DomainArchiveDeployer appDomainDeployer) {
        SingleAppDomainDeployerBuilder singleAppDomainDeployerBuilder = mock(SingleAppDomainDeployerBuilder.class);
        when(singleAppDomainDeployerBuilder.withDomains(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withApplicationDeployer(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withDomainFactory(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withDomainArtifactDeployer(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withApplicationFactory(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withApplications(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withDeploymentService(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withApplicationArtifactDeployer(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withApplicationDeploymentListener(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.withDomainDeploymentListener(any())).thenReturn(singleAppDomainDeployerBuilder);
        when(singleAppDomainDeployerBuilder.build()).thenReturn(appDomainDeployer);
        return singleAppDomainDeployerBuilder;
    }
}

