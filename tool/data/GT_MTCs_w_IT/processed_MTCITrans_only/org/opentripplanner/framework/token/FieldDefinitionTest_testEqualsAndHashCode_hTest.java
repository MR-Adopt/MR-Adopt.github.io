package org.opentripplanner.framework.token;

import org.opentripplanner.framework.token.FieldDefinition;
import org.opentripplanner.framework.token.FieldDefinition.*;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

class FieldDefinitionTest_testEqualsAndHashCode_hTest {

  public static String NAME = "foo";
  public static TokenType TOKEN_TYPE = TokenType.STRING;
  public FieldDefinition subject = new FieldDefinition(NAME, TOKEN_TYPE);

  @Test
  void testEqualsAndHashCode_h() {
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);

    var same = new FieldDefinition(NAME, TOKEN_TYPE);
    var other1 = new FieldDefinition(NAME, TokenType.INT);
    var other2 = new FieldDefinition("Bar", TOKEN_TYPE);
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();

    assertEquals(subject, subject);
    assertEquals(same, subject);
    assertNotEquals(other1, subject);
    assertNotEquals(other2, subject);
    assertNotEquals(other3, subject);

    assertEquals(same.hashCode(), subject.hashCode());
    assertNotEquals(other1.hashCode(), subject.hashCode());
    assertNotEquals(other2.hashCode(), subject.hashCode());
    assertNotEquals(other3.hashCode(), subject.hashCode());
  }
}