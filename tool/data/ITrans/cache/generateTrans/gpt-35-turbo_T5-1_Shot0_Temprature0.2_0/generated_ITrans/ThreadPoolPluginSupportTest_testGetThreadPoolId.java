package cn.hippo4j.core.executor.plugin.manager;

import cn.hippo4j.core.executor.ExtensibleThreadPoolExecutor;
import cn.hippo4j.core.executor.plugin.ExecuteAwarePlugin;
import cn.hippo4j.core.executor.plugin.RejectedAwarePlugin;
import cn.hippo4j.core.executor.plugin.ShutdownAwarePlugin;
import cn.hippo4j.core.executor.plugin.TaskAwarePlugin;
import cn.hippo4j.core.executor.plugin.ThreadPoolPlugin;
import cn.hippo4j.core.executor.plugin.manager.DefaultThreadPoolPluginManager;
import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginManager;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.junit.Assert;
import org.junit.Test;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;


import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupport;
import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupport.*;
import java.util.List;
import java.util.Arrays;

public class ThreadPoolPluginSupportTest_testGetThreadPoolId {
    public static ThreadPoolPluginSupport inputTransformation_testGetThreadPoolId(ExtensibleThreadPoolExecutor executor)  {
        ThreadPoolPluginSupport support = new ThreadPoolPluginSupport(executor.getThreadPoolId(), executor, manager);
        return support;
    }
}