package org.opentripplanner.framework.token;

import org.opentripplanner.framework.token.FieldDefinition;
import org.opentripplanner.framework.token.FieldDefinition.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

class FieldDefinitionTest_testEqualsAndHashCode_h1Test3 {

    public static String NAME = "foo";

    public static TokenType TOKEN_TYPE = TokenType.STRING;

    public FieldDefinition subject = new FieldDefinition(NAME, TOKEN_TYPE);

    @Test
    void testEqualsAndHashCode_h1Test3() {
    FieldDefinition subject = new FieldDefinition(null, TokenType.STRING);
    FieldDefinition other3 = new FieldDefinition(null, TokenType.STRING).deprecate();
        var same = new FieldDefinition(NAME, TOKEN_TYPE);
        var other1 = new FieldDefinition(NAME, TokenType.INT);
        var other2 = new FieldDefinition("Bar", TOKEN_TYPE);
        assertNotEquals(other3.hashCode(), subject.hashCode());
    }
}

