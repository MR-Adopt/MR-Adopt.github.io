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
SOURCE INPUT: `job2Detail`
FOLLOW UP INPUT: `job22`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).build();
```

## New source input1:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably(false).build();
```

## New source input2:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().requestRecovery().build();
```

## New source input3:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().requestRecovery(false).build();
```

## New source input4:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).withDescription("New job description").storeDurably().build();
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    JobDetail job2Detail = newJob(HelloJob.class).withIdentity(new JobKey("job2", GROUP_KEY)).storeDurably().build();
    JobKey job22 = new JobKey("job2", GROUP_KEY);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.