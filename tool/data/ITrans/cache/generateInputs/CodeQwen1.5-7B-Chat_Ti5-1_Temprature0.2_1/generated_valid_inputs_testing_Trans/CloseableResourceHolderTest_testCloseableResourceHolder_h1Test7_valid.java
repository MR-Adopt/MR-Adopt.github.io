/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.druid.collections;

import org.apache.druid.collections.CloseableResourceHolderTest_testCloseableResourceHolder;

import org.apache.druid.collections.ResourceHolder;
import org.apache.druid.collections.ResourceHolder.*;
import org.junit.Assert;
import org.junit.Test;
import java.io.Closeable;
import java.util.concurrent.atomic.AtomicLong;

public class CloseableResourceHolderTest_testCloseableResourceHolder_h1Test7_valid {

    @Test
    public void testCloseableResourceHolder_h1Test7() {
        AtomicLong closeCounter = new AtomicLong();
    Closeable closeable = new Closeable() {
        @Override
        public void close() throws IOException {
            // Do nothing
        }
    ResourceHolder<Closeable> holder2  = CloseableResourceHolderTest_testCloseableResourceHolder.inputTransformation_testCloseableResourceHolder(closeable);
        ResourceHolder<Closeable> holder = ResourceHolder.fromCloseable(closeable);
        Assert.assertSame(closeable, holder2.get());
    }
}

