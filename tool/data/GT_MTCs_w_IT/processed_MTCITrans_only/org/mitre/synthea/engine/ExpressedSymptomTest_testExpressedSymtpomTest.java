package org.mitre.synthea.engine;

import org.mitre.synthea.engine.ExpressedSymptom;
import org.mitre.synthea.engine.ExpressedSymptom.*;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;
import org.mitre.synthea.engine.ExpressedSymptom.SymptomInfo;
import org.mitre.synthea.engine.ExpressedSymptom.SymptomSource;

public class ExpressedSymptomTest_testExpressedSymtpomTest {

//   @Test
//   public void testExpressedSymtpom_h() {
//     String name = "pain";
//     ExpressedSymptom symptom = new ExpressedSymptom(name);
//     String module = "testModule"; symptom.addressSource(module);
// 
//     ExpressedSymptom symptom2 = symptom;
//     String module2 = "testModule"; symptom2.addressSource(module2);
// 
// 
//     String cause = "testCause";
//     for (long l = 0L; l < 3L; l++) {
//       symptom.onSet(module, cause, l, (int) (100 * l), false);
//       assertEquals(module, symptom.getSourceWithHighValue());
//       assertEquals(Integer.valueOf((int) (100 * l)), symptom.getValueFromSource(module));
//       assertEquals((int) (100 * l), symptom.getSymptom());
//       assertEquals(Long.valueOf(l), symptom2.getSymptomLastUpdatedTime(module2));
//     }
//   }
// 
// //   public static List<Object> inputTransformation_testExpressedSymtpom(ExpressedSymptom symptom, String module) {
// //     ExpressedSymptom symptom2 = symptom;
// //     String module2 = "testModule"; 
// //     symptom2.addressSource(module2);
// //     List<Object> follow_up_inputs = Arrays.asList(symptom2, module2);
// // 		return follow_up_inputs;
// //   }
// // 
  @Test
  public void testExpressedSymtpom_IT() {
    String name = "pain";
    ExpressedSymptom symptom = new ExpressedSymptom(name);
    String module = "testModule"; symptom.addressSource(module);

    List<Object> transformed_inputs = ExpressedSymptomTest_testExpressedSymtpom.inputTransformation_testExpressedSymtpom(symptom, module);
    ExpressedSymptom symptom2 = (ExpressedSymptom) transformed_inputs.get(0);
    String module2 = (String) transformed_inputs.get(1);

    String cause = "testCause";
    for (long l = 0L; l < 3L; l++) {
      symptom.onSet(module, cause, l, (int) (100 * l), false);
      assertEquals(module, symptom.getSourceWithHighValue());
      assertEquals(Integer.valueOf((int) (100 * l)), symptom.getValueFromSource(module));
      assertEquals((int) (100 * l), symptom.getSymptom());
      assertEquals(Long.valueOf(l), symptom2.getSymptomLastUpdatedTime(module2));
    }
  }
}