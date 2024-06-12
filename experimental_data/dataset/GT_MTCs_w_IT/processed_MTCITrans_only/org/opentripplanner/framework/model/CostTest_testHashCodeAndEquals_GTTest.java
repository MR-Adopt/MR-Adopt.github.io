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

class CostTest_testHashCodeAndEquals_GTTest {

  public static final int VALUE_SECONDS = 10;
  public Cost subject = Cost.costOfSeconds(VALUE_SECONDS);

//   @Test
//   void testHashCodeAndEquals_h() {
//     Cost subject = Cost.costOfSeconds(10);
//     Cost same = Cost.costOfSeconds(10);
//     assertEquals(subject, same);
//     assertEquals(subject.hashCode(), same.hashCode());
// 
//     Cost other = Cost.costOfSeconds(11);
//     assertNotEquals(subject, other);
//     assertNotEquals(subject.hashCode(), other.hashCode());
//   }
// 
// //   public static Cost inputTransformation_testHashCodeAndEquals(Cost subject) {
// //     Cost other = subject.multiply(1.1);
// //     return other;
// //   }
// // 
  @Test
  void testHashCodeAndEquals_IT() {
    Cost subject = Cost.costOfSeconds(10);
    Cost same = Cost.costOfSeconds(10);
    assertEquals(subject, same);
    assertEquals(subject.hashCode(), same.hashCode());

    Cost other = CostTest_testHashCodeAndEquals_GT.inputTransformation_testHashCodeAndEquals(subject);
    assertNotEquals(subject, other);
    assertNotEquals(subject.hashCode(), other.hashCode());
  }

}