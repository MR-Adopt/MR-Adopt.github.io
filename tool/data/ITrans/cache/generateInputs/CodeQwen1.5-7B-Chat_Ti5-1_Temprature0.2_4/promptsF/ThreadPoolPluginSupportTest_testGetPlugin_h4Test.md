# ORIGINAL TEST CASE
```java
@Test
public void testGetPlugin() {
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin();
    support.register(plugin);
    String pluginId = "TestExecuteAwarePlugin";
    Assert.assertSame(plugin, support.getPlugin(pluginId).orElse(null));
}

```
SOURCE INPUT: `plugin`
FOLLOW UP INPUT: `pluginId`


# METHOD UNDER TEST
```java
/**
 * Register a {@link ThreadPoolPlugin}
 *
 * @param plugin aware
 */
@Override
default void register(ThreadPoolPlugin plugin) {
    getThreadPoolPluginManager().register(plugin);
}

/**
 * Get {@link ThreadPoolPlugin}.
 *
 * @param pluginId target name
 * @return {@link ThreadPoolPlugin}, null if unregister
 * @throws ClassCastException thrown when the object obtained by name cannot be converted to target type
 */
@Override
default <A extends ThreadPoolPlugin> Optional<A> getPlugin(String pluginId) {
    return getThreadPoolPluginManager().getPlugin(pluginId);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin("CustomPluginId");
```

## New source input1:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin(null);
```

## New source input2:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin("");
```

## New source input3:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin(new Object());
```

## New source input4:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin(123);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin();
    String pluginId = "TestExecuteAwarePlugin";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.