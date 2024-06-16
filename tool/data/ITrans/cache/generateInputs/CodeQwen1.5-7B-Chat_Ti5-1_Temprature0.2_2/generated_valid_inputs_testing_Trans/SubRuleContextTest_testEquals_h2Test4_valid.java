package software.amazon.event.ruler;

import software.amazon.event.ruler.SubRuleContextTest_testEquals;

import software.amazon.event.ruler.SubRuleContext;
import software.amazon.event.ruler.SubRuleContext.*;
import org.junit.Test;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

public class SubRuleContextTest_testEquals_h2Test4_valid {

    private static final String NAME = "name";

    @Test
    public void testEquals_h2Test4() {
    String NAME = "name5";
    SubRuleContext.Generator generatorA = new SubRuleContext.Generator();
		List<Object> transformed_inputs = SubRuleContextTest_testEquals.inputTransformation_testEquals(generatorA, NAME);
    String NAME2  = (String) transformed_inputs.get(1);
    SubRuleContext.Generator generatorB  = (SubRuleContext.Generator) transformed_inputs.get(0);
        SubRuleContext contextA1 = generatorA.generate(NAME);
        // SubRuleContext contextA2 = generatorA.generate(NAME);
        SubRuleContext contextB1 = generatorB.generate(NAME2);
        assertTrue(contextA1.equals(contextB1));
    // assertFalse(contextA2.equals(contextB1));
    }
}

