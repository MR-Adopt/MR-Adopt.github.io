package software.amazon.event.ruler;

import software.amazon.event.ruler.SubRuleContext.SubRuleContextTest_testGetters_GT;

import software.amazon.event.ruler.SubRuleContext;

import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

public class SubRuleContextTest_testGetters_GTTest {

    private static final String NAME = "name";

//     @Test
//     public void testGetters_h() {
//         SubRuleContext.Generator generator = new SubRuleContext.Generator();
//         SubRuleContext context = generator.generate(NAME);
//         Double id = -1.7976931348623157E308;
//         SubRuleContext.Generator generator2 = new SubRuleContext.Generator();
//         generator2.generate("name");
//         assertEquals(NAME, generator2.getNameForGeneratedId(id));
//         Set<Double> expectedIds = new HashSet<>();
//         expectedIds.add(context.getId());
//         assertEquals(expectedIds, generator.getIdsGeneratedForName(NAME));
//     }
// 
    @Test
    public void testGetters_IT() {
        SubRuleContext.Generator generator = new SubRuleContext.Generator();
        SubRuleContext context = generator.generate(NAME);
        List<Object> follow_up_inputs = SubRuleContextTest_testGetters_GT.inputTransformation_testGetters(generator, NAME);
        SubRuleContext.Generator generator2 = (SubRuleContext.Generator) follow_up_inputs.get(0);
        Double id = (Double) follow_up_inputs.get(1);
        assertEquals(NAME, generator2.getNameForGeneratedId(id));
        Set<Double> expectedIds = new HashSet<>();
        expectedIds.add(context.getId());
        assertEquals(expectedIds, generator.getIdsGeneratedForName(NAME));
    }

//     public static List<Object> inputTransformation_testGetters(SubRuleContext.Generator generator, String NAME) {
//         SubRuleContext.Generator generator2 = new SubRuleContext.Generator();
//         SubRuleContext context = generator2.generate(NAME);
//         Double id = context.getId();
//         List<Object> follow_up_inputs = Arrays.asList(generator2, id);
//         return follow_up_inputs;
//     }
// 
// 
}