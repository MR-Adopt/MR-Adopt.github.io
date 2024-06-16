package org.quartz.impl;

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
import java.util.Properties;
import javax.management.AttributeList;
import javax.management.MBeanServer;
import javax.management.MalformedObjectNameException;
import javax.management.ObjectName;


import org.quartz.impl.RemoteMBeanScheduler;
import org.quartz.impl.RemoteMBeanScheduler.*;
import java.util.List;
import java.util.Arrays;

public class RemoteMBeanSchedulerTest_testJobOperations {
    public static JobKey inputTransformation_testJobOperations(JobDetail job2Detail) {
        String jobName = job2Detail.getKey().getName();
        JobKey job22 = new JobKey(jobName, GROUP_KEY);
        return job22;
    }
}