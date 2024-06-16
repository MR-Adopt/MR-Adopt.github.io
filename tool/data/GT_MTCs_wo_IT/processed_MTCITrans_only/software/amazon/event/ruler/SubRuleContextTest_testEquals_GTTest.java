package software.amazon.event.ruler;

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

public class SubRuleContextTest_testEquals_GTTest {

    private static final String NAME = "name";

//     @Test
//     public void testEquals_h() {
//         String NAME = "name";
//         SubRuleContext.Generator generatorA = new SubRuleContext.Generator();
//         SubRuleContext contextA1 = generatorA.generate(NAME);
//         // SubRuleContext contextA2 = generatorA.generate(NAME);
//         
//         String NAME2 = "name";
//         SubRuleContext.Generator generatorB = new SubRuleContext.Generator();
//         SubRuleContext contextB1 = generatorB.generate(NAME2);
// 
//         assertTrue(contextA1.equals(contextB1));
//         // assertFalse(contextA2.equals(contextB1));
//     }
// 
// //     public static List<Object> inputTransformation_testEquals( SubRuleContext.Generator generatorA, String NAME) {
// // 		String NAME2 = NAME;
// //         SubRuleContext.Generator generatorB = new SubRuleContext.Generator();
// // 		List<Object> transformed_inputs = Arrays.asList(generatorB, NAME2);
// // 		return transformed_inputs;
// // 	}
// // 
    @Test
    public void testEquals_IT() {
        String NAME = "name";
        SubRuleContext.Generator generatorA = new SubRuleContext.Generator();
        SubRuleContext contextA1 = generatorA.generate(NAME);
        // SubRuleContext contextA2 = generatorA.generate(NAME);
        
        List<Object> transformed_inputs = SubRuleContextTest_testEquals_GT.inputTransformation_testEquals(generatorA, NAME);
        SubRuleContext.Generator generatorB = (SubRuleContext.Generator) transformed_inputs.get(0);
        String NAME2 = (String) transformed_inputs.get(1);
        SubRuleContext contextB1 = generatorB.generate(NAME2);

        assertTrue(contextA1.equals(contextB1));
        // assertFalse(contextA2.equals(contextB1));
    }

}