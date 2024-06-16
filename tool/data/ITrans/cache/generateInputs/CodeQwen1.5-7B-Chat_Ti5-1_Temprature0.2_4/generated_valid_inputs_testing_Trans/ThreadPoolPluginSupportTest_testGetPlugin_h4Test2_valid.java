/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package cn.hippo4j.core.executor.plugin.manager;

import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupportTest_testGetPlugin;

import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupport.*;
import cn.hippo4j.core.executor.ExtensibleThreadPoolExecutor;
import cn.hippo4j.core.executor.plugin.ExecuteAwarePlugin;
import cn.hippo4j.core.executor.plugin.RejectedAwarePlugin;
import cn.hippo4j.core.executor.plugin.ShutdownAwarePlugin;
import cn.hippo4j.core.executor.plugin.TaskAwarePlugin;
import cn.hippo4j.core.executor.plugin.ThreadPoolPlugin;
import cn.hippo4j.core.executor.plugin.manager.DefaultThreadPoolPluginManager;
import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginManager;
import cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupport;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.junit.Assert;
import org.junit.Test;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * test for default method of {@link ThreadPoolPluginSupport}
 */
public class ThreadPoolPluginSupportTest_testGetPlugin_h4Test2_valid {

    private final ThreadPoolPluginManager manager = new DefaultThreadPoolPluginManager();

    private final ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());

    private final ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);

    @Getter
    @RequiredArgsConstructor
    private static class TestSupport implements ThreadPoolPluginSupport {

        private final String threadPoolId;

        private final ExtensibleThreadPoolExecutor threadPoolExecutor;

        private final ThreadPoolPluginManager threadPoolPluginManager;
    }

    @Test
    public void testGetPlugin_h4Test2() {
    ThreadPoolPlugin plugin = new TestExecuteAwarePlugin("");
    String pluginId  = ThreadPoolPluginSupportTest_testGetPlugin.inputTransformation_testGetPlugin(plugin);
        support.register(plugin);
        Assert.assertSame(plugin, support.getPlugin(pluginId).orElse(null));
    }

    // ================ default delegate method ================
    @Getter
    private final static class TestTaskAwarePlugin implements TaskAwarePlugin {

        private final String id = this.getClass().getSimpleName();
    }

    @Getter
    private final static class TestExecuteAwarePlugin implements ExecuteAwarePlugin {

        private final String id = this.getClass().getSimpleName();
    }

    @Getter
    private final static class TestRejectedAwarePlugin implements RejectedAwarePlugin {

        private final String id = this.getClass().getSimpleName();
    }

    @Getter
    private final static class TestShutdownAwarePlugin implements ShutdownAwarePlugin {

        private final String id = this.getClass().getSimpleName();
    }
}

