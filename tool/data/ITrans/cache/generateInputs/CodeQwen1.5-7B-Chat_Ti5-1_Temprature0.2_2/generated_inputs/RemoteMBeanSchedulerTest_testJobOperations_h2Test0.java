/*
 * All content copyright Terracotta, Inc., unless otherwise indicated. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.quartz.impl;

import org.quartz.impl.RemoteMBeanScheduler;
import org.quartz.impl.RemoteMBeanScheduler.*;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.CoreMatchers.notNullValue;
import static org.hamcrest.CoreMatchers.nullValue;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.fail;
import static org.quartz.JobBuilder.newJob;
import static org.quartz.TriggerBuilder.newTrigger;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.quartz.Job;
import org.quartz.JobDetail;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.quartz.JobKey;
import org.quartz.Scheduler;
import org.quartz.SchedulerException;
import org.quartz.SchedulerMetaData;
import org.quartz.Trigger;
import org.quartz.TriggerKey;
import org.quartz.core.QuartzSchedulerResources;
import org.quartz.impl.calendar.BaseCalendar;
import org.quartz.impl.matchers.GroupMatcher;
import java.lang.management.ManagementFactory;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Properties;
import javax.management.AttributeList;
import javax.management.MBeanServer;
import javax.management.MalformedObjectNameException;
import javax.management.ObjectName;

/**
 * RemoteMBeanSchedulerTest_testJobOperations_h2Test0
 */
public class RemoteMBeanSchedulerTest_testJobOperations_h2Test0 {

    public static final String TRIGGER_KEY = "trigger1";

    public static final String GROUP_KEY = "group1";

    public static final String JOB_KEY = "job1";

    public static final String CALENDAR_KEY = "calendar1";

    private Scheduler scheduler;

    private RemoteMBeanScheduler remoteScheduler;

    @Before
    public void setUp() throws Exception {
        Properties props = new Properties();
        props.put("org.quartz.scheduler.instanceName", "TestScheduler");
        props.put("org.quartz.jobStore.class", "org.quartz.simpl.RAMJobStore");
        props.put("org.quartz.threadPool.class", "org.quartz.simpl.SimpleThreadPool");
        props.put("org.quartz.threadPool.threadCount", "1");
        props.put("org.quartz.scheduler.jmx.export", "true");
        scheduler = new StdSchedulerFactory(props).getScheduler();
        JobDetail jobDetail = newJob(HelloJob.class).withIdentity(JOB_KEY, GROUP_KEY).build();
        Trigger trigger = newTrigger().withIdentity(TRIGGER_KEY, GROUP_KEY).startAt(new Date()).build();
        scheduler.addCalendar(CALENDAR_KEY, new BaseCalendar(), false, false);
        scheduler.scheduleJob(jobDetail, trigger);
        String objectName = QuartzSchedulerResources.generateJMXObjectName(scheduler.getSchedulerName(), scheduler.getSchedulerInstanceId());
        remoteScheduler = new TestRemoteScheduler(objectName);
    }

    @After
    public void tearDown() throws SchedulerException {
        scheduler.shutdown();
    }

    @Test
    public void testJobOperations_h2Test0() throws Exception {
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().build();
    JobKey job22 = new JobKey("job2", GROUP_KEY);
        remoteScheduler.addJob(job2Detail, false);
        assertThat(remoteScheduler.getJobDetail(job22), equalTo(job2Detail));
    }

    public static class HelloJob implements Job {

        public void execute(JobExecutionContext context) throws JobExecutionException {
            System.out.println("hello world!");
        }
    }

    public static class TestRemoteScheduler extends RemoteMBeanScheduler {

        private MBeanServer mBeanServer;

        private ObjectName objectName;

        public TestRemoteScheduler(String objectName) throws SchedulerException, MalformedObjectNameException {
            this.objectName = new ObjectName(objectName);
            initialize();
        }

        @Override
        public void initialize() throws SchedulerException {
            mBeanServer = ManagementFactory.getPlatformMBeanServer();
        }

        @Override
        protected Object getAttribute(String attribute) throws SchedulerException {
            try {
                return mBeanServer.getAttribute(objectName, attribute);
            } catch (Exception e) {
                throw new SchedulerException(e);
            }
        }

        @Override
        protected AttributeList getAttributes(String[] attributes) throws SchedulerException {
            try {
                return mBeanServer.getAttributes(objectName, attributes);
            } catch (Exception e) {
                throw new SchedulerException(e);
            }
        }

        @Override
        protected Object invoke(String operationName, Object[] params, String[] signature) throws SchedulerException {
            try {
                return mBeanServer.invoke(objectName, operationName, params, signature);
            } catch (Exception e) {
                throw new SchedulerException(e);
            }
        }
    }
}

