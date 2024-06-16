package org.opentripplanner.framework.model;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.opentripplanner.framework.model.Cost.ONE_HOUR_WITH_TRANSIT;
import java.time.Duration;
import java.util.stream.Stream;
import org.junit.jupiter.api.Test;


import org.opentripplanner.framework.model.Cost;
import org.opentripplanner.framework.model.Cost.*;
import java.util.List;
import java.util.Arrays;

public class CostTest_testHashCodeAndEquals {
    public static Cost inputTransformation_testHashCodeAndEquals(Cost subject)  {
        int newValue = subject.getValue() + 1;
        Cost other = Cost.costOfSeconds(newValue);
        return other;
    }
}