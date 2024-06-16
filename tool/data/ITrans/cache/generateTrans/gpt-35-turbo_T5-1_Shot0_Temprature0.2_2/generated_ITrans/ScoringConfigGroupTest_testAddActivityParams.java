package org.matsim.core.config.groups;

import static org.matsim.core.config.groups.ScoringConfigGroup.createStageActivityType;
import java.util.Map;
import java.util.Random;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.RegisterExtension;
import org.matsim.api.core.v01.TransportMode;
import org.matsim.core.config.Config;
import org.matsim.core.config.ConfigGroup;
import org.matsim.core.config.ConfigReader;
import org.matsim.core.config.ConfigUtils;
import org.matsim.core.config.ConfigWriter;
import org.matsim.core.config.groups.ScoringConfigGroup.ActivityParams;
import org.matsim.core.config.groups.ScoringConfigGroup.ModeParams;
import org.matsim.testcases.MatsimTestUtils;


import org.matsim.core.config.groups.ScoringConfigGroup;
import org.matsim.core.config.groups.ScoringConfigGroup.*;
import java.util.List;
import java.util.Arrays;

public class ScoringConfigGroupTest_testAddActivityParams {
    public static String inputTransformation_testAddActivityParams(ActivityParams ap) {
        String type = ap.getActivityType();
        return type;
    }
}