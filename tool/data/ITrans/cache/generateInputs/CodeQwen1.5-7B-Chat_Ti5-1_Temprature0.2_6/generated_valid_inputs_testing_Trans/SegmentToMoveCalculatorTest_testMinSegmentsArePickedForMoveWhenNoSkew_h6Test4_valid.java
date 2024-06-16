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
package org.apache.druid.server.coordinator.balancer;

import org.apache.druid.server.coordinator.balancer.SegmentToMoveCalculatorTest_testMinSegmentsArePickedForMoveWhenNoSkew;

import org.apache.druid.server.coordinator.balancer.SegmentToMoveCalculator;
import org.apache.druid.server.coordinator.balancer.SegmentToMoveCalculator.*;
import org.apache.druid.client.DruidServer;
import org.apache.druid.java.util.common.granularity.Granularities;
import org.apache.druid.server.coordination.ServerType;
import org.apache.druid.server.coordinator.CreateDataSegments;
import org.apache.druid.server.coordinator.ServerHolder;
import org.apache.druid.server.coordinator.loading.TestLoadQueuePeon;
import org.apache.druid.timeline.DataSegment;
import org.joda.time.Duration;
import org.junit.Assert;
import org.junit.Test;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SegmentToMoveCalculatorTest_testMinSegmentsArePickedForMoveWhenNoSkew_h6Test4_valid {

    private static final Duration DEFAULT_COORDINATOR_PERIOD = Duration.standardMinutes(1);

    /**
     * 100 days x 100 partitions = 10,000 segments.
     */
    private static final List<DataSegment> WIKI_SEGMENTS = CreateDataSegments.ofDatasource("wiki").forIntervals(100, Granularities.DAY).withNumPartitions(100).eachOfSizeInMb(500);

    /**
     * 10 days * 1 partitions = 10 segments.
     */
    private static final List<DataSegment> KOALA_SEGMENTS = CreateDataSegments.ofDatasource("koala").forIntervals(10, Granularities.DAY).eachOfSizeInMb(500);

    private static final String TIER = "tier1";

    @Test
    public void testMinSegmentsArePickedForMoveWhenNoSkew_h6Test4() {
    int totalSegmentsInTier = 10_000_000;
		List<Object> transformed_inputs = SegmentToMoveCalculatorTest_testMinSegmentsArePickedForMoveWhenNoSkew.inputTransformation_testMinSegmentsArePickedForMoveWhenNoSkew(totalSegmentsInTier);
    String tier  = (String) transformed_inputs.get(0);
    List<ServerHolder> historicals  = (List<ServerHolder>) transformed_inputs.get(1);
    int maxSegmentsToMoveInTier  = (int) transformed_inputs.get(2);
        int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
        // Find segmentsToMove with no limit on maxSegmentsToMove
        int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
        // System.out.println("minSegmentsToMove: " + minSegmentsToMove);
        // System.out.println("segmentsToMove: " + segmentsToMove);
        Assert.assertEquals(minSegmentsToMove, segmentsToMove);
    }

    private static int computeMaxSegmentsToMove(int totalSegments, int numThreads) {
        return SegmentToMoveCalculator.computeMaxSegmentsToMovePerTier(totalSegments, numThreads, DEFAULT_COORDINATOR_PERIOD);
    }

    private static int computeMaxSegmentsToMoveInPeriod(int totalSegments, Duration coordinatorPeriod) {
        return SegmentToMoveCalculator.computeMaxSegmentsToMovePerTier(totalSegments, 1, coordinatorPeriod);
    }

    private static int computeMinSegmentsToMove(int totalSegmentsInTier) {
        return SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    }

    private static ServerHolder createServer(String name, List<DataSegment> segments) {
        final DruidServer server = new DruidServer(name, name, null, 10L << 30, ServerType.HISTORICAL, "tier1", 1);
        segments.forEach(server::addDataSegment);
        return new ServerHolder(server.toImmutableDruidServer(), new TestLoadQueuePeon());
    }
}

