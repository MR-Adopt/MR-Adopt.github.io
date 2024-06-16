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
package org.apache.dubbo.config.bootstrap.builders;

import org.apache.dubbo.config.bootstrap.builders.MetricsBuilder;
import org.apache.dubbo.config.bootstrap.builders.MetricsBuilder.*;

import org.apache.dubbo.config.MetricsConfig;
import org.apache.dubbo.config.nested.AggregationConfig;
import org.apache.dubbo.config.nested.HistogramConfig;
import org.apache.dubbo.config.nested.PrometheusConfig;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

class MetricsBuilderTest_aggregation_hTest {

    @Test
    void aggregation_h() {
        AggregationConfig aggregation = new AggregationConfig();
        aggregation.setEnabled(true);
        aggregation.setEnableQps(false);
        aggregation.setBucketNum(100);
        AggregationConfig aggregation2 = aggregation;

        MetricsBuilder builder = MetricsBuilder.newBuilder();
        builder.aggregation(aggregation);

        MetricsBuilder builder2 = MetricsBuilder.newBuilder();
        builder2.aggregation(aggregation2);

        Assertions.assertSame(aggregation, builder2.build().getAggregation());
        Assertions.assertTrue(builder.build().getAggregation().getEnabled());
        Assertions.assertFalse(builder.build().getAggregation().getEnableQps());
        Assertions.assertEquals(100, builder.build().getAggregation().getBucketNum());
    }
}