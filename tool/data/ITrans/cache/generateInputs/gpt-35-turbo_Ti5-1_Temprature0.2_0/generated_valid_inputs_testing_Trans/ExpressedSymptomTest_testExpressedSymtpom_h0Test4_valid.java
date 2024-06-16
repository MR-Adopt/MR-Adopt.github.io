package org.mitre.synthea.engine;

import org.mitre.synthea.engine.ExpressedSymptomTest_testExpressedSymtpom;

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

public class ExpressedSymptomTest_testExpressedSymtpom_h0Test4_valid {

    @Test
    public void testExpressedSymtpom_h0Test4() {
String name = "nausea";
ExpressedSymptom symptom = new ExpressedSymptom(name);
String module = "module5";
symptom.addressSource(module);
		List<Object> transformed_inputs = ExpressedSymptomTest_testExpressedSymtpom.inputTransformation_testExpressedSymtpom(symptom, module);
ExpressedSymptom symptom2  = (ExpressedSymptom) transformed_inputs.get(0);
String module2  = (String) transformed_inputs.get(1);
symptom2.addressSource(module2);
        String cause = "testCause";
        for (long l = 0L; l < 3L; l++) {
            symptom.onSet(module, cause, l, (int) (100 * l), false);
            assertEquals(Long.valueOf(l), symptom2.getSymptomLastUpdatedTime(module2));
        }
    }
}

