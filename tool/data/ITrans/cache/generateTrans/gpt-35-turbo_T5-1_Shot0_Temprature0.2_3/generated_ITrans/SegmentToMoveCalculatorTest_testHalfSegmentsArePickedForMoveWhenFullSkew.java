package org.apache.druid.server.coordinator.balancer;

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
import java.util.Collections;


import org.apache.druid.server.coordinator.balancer.SegmentToMoveCalculator;
import org.apache.druid.server.coordinator.balancer.SegmentToMoveCalculator.*;
import java.util.List;
import java.util.Arrays;

public class SegmentToMoveCalculatorTest_testHalfSegmentsArePickedForMoveWhenFullSkew {
    public static List<Object> inputTransformation_testHalfSegmentsArePickedForMoveWhenFullSkew(String tier, List<ServerHolder> historicals) {
        String tier2 = tier;
        List<ServerHolder> historicals2 = historicals;
        int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
        List<Object> transformed_inputs = Arrays.asList(tier2, historicals2, maxSegmentsToMoveInTier);
        return transformed_inputs;
    }
}