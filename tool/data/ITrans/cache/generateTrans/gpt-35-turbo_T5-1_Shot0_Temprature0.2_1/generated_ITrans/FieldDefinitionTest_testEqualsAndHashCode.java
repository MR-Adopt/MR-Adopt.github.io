package org.opentripplanner.framework.token;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;


import org.opentripplanner.framework.token.FieldDefinition;
import org.opentripplanner.framework.token.FieldDefinition.*;
import java.util.List;
import java.util.Arrays;

public class FieldDefinitionTest_testEqualsAndHashCode {
    public static FieldDefinition inputTransformation_testEqualsAndHashCode(FieldDefinition subject)  {
        FieldDefinition other3 = new FieldDefinition(subject.getName(), subject.getType()).deprecate();
        return other3;
    }
}