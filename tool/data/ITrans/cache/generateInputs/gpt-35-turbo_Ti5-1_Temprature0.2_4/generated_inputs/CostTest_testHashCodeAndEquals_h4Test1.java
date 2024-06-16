package org.opentripplanner.framework.model;

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

class CostTest_testHashCodeAndEquals_h4Test1 {

    public static final int VALUE_SECONDS = 10;

    public Cost subject = Cost.costOfSeconds(VALUE_SECONDS);

    @Test
    void testHashCodeAndEquals_h4Test1() {
    Cost subject = Cost.costOfSeconds(-10);
    Cost other = Cost.costOfSeconds(-11);
        Cost same = Cost.costOfSeconds(10);
        assertNotEquals(subject.hashCode(), other.hashCode());
    }
}

