package org.opentripplanner.framework.model;

import org.opentripplanner.framework.model.CostTest_testHashCodeAndEquals;

import org.opentripplanner.framework.model.Cost;
import org.opentripplanner.framework.model.Cost.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.opentripplanner.framework.model.Cost.ONE_HOUR_WITH_TRANSIT;
import java.time.Duration;
import java.util.List;
import java.util.stream.Stream;
import org.junit.jupiter.api.Test;

class CostTest_testHashCodeAndEquals_h1Test3_valid {

    public static final int VALUE_SECONDS = 10;

    public Cost subject = Cost.costOfSeconds(VALUE_SECONDS);

    @Test
    void testHashCodeAndEquals_h1Test3() {
    Cost subject = Cost.costOfSeconds(1000000);
    Cost other  = CostTest_testHashCodeAndEquals.inputTransformation_testHashCodeAndEquals(subject);
        Cost same = Cost.costOfSeconds(10);
        assertNotEquals(subject.hashCode(), other.hashCode());
    }
}

