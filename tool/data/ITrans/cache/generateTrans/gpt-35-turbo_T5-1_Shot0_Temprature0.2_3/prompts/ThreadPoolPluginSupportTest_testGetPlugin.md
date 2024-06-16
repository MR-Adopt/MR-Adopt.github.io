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


# TEST CASE
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


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class ThreadPoolPluginSupportTest_testGetPlugin {
    public static String inputTransformation_testGetPlugin(ThreadPoolPlugin plugin)  {
        // TODO
        String pluginId = 
		return pluginId;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.