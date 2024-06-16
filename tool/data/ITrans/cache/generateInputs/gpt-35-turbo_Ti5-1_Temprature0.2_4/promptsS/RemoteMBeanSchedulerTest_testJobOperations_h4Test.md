# ORIGINAL TEST CASE
```java
@Test
public void testJobOperations() throws Exception {
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().build();
    remoteScheduler.addJob(job2Detail, false);
    JobKey job22 = new JobKey("job2", GROUP_KEY);
    assertThat(remoteScheduler.getJobDetail(job22), equalTo(job2Detail));
}

```
TEST INPUT: `job2Detail`


# METHOD UNDER TEST
```java
/**
 * <p>
 * Calls the equivalent method on the 'proxied' <code>QuartzScheduler</code>,
 * passing the <code>SchedulingContext</code> associated with this
 * instance.
 * </p>
 */
public void addJob(JobDetail jobDetail, boolean replace, boolean storeNonDurableWhileAwaitingScheduling) throws SchedulerException {
    invoke("addJob", new Object[] { JobDetailSupport.toCompositeData(jobDetail), replace, storeNonDurableWhileAwaitingScheduling }, new String[] { CompositeData.class.getName(), boolean.class.getName(), boolean.class.getName() });
}

/**
 * <p>
 * Calls the equivalent method on the 'proxied' <code>QuartzScheduler</code>,
 * passing the <code>SchedulingContext</code> associated with this
 * instance.
 * </p>
 */
public JobDetail getJobDetail(JobKey jobKey) throws SchedulerException {
    try {
        return JobDetailSupport.newJobDetail((CompositeData) invoke("getJobDetail", new Object[] { jobKey.getName(), jobKey.getGroup() }, new String[] { String.class.getName(), String.class.getName() }));
    } catch (ClassNotFoundException e) {
        throw new SchedulerException("Unable to resolve job class", e);
    }
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `job2Detail`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().build();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 