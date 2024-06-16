package org.mule.runtime.module.deployment.test.internal.singleapp;

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
import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDomainDeployerBuilder;
import org.mule.tck.junit4.AbstractMuleTestCase;
import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.util.ArrayList;
import java.util.Properties;
import java.util.function.Consumer;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;


import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDeploymentService;
import org.mule.runtime.module.deployment.internal.singleapp.SingleAppDeploymentService.*;
import java.util.List;
import java.util.Arrays;

public class SingleAppDeploymentServiceTestCase_startupListeners {
    public static StartupListener inputTransformation_startupListeners(StartupListener startUpListener1)  {
        // Transformation function: return the source input itself
        StartupListener startUpListener2 = startUpListener1;
        return startUpListener2;
    }
}