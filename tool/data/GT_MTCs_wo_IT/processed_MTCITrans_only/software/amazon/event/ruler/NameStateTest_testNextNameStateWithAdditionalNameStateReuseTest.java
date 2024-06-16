package software.amazon.event.ruler;

import software.amazon.event.ruler.NameState;
import software.amazon.event.ruler.NameState.*;

import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static java.util.Arrays.asList;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

public class NameStateTest_testNextNameStateWithAdditionalNameStateReuseTest {

//     @Test
//     public void testNextNameStateWithAdditionalNameStateReuse_h() {
//         NameState nameState = new NameState();
//         NameState nextNameState = new NameState();
//         String key = "key";
//         String key2 = "key";
//         NameState nameState2 = nameState;
//         nameState.addNextNameState(key, nextNameState);
//         assertEquals(nextNameState, nameState2.getNextNameState(key2));
// 
//         // nameState.removeNextNameState("key");
//         // assertNull(nameState.getNextNameState("key"));
//     }
// 
// //     public static List<Object> inputTransformation_testNextNameStateWithAdditionalNameStateReuse(String key, NameState nextNameState ) {
// //         String key2 = key;
// //         NameState nameState2  = new NameState();
// //         nameState2.addNextNameState(key2, nextNameState);
// //         List<Object> transformed_inputs = Arrays.asList(key2, nameState2);
// // 		return transformed_inputs;
// //     }
// // 
    @Test
    public void testNextNameStateWithAdditionalNameStateReuse_IT() {
        NameState nameState = new NameState();
        NameState nextNameState = new NameState();
        String key = "key";

        List<Object> transformed_inputs = NameStateTest_testNextNameStateWithAdditionalNameStateReuse.inputTransformation_testNextNameStateWithAdditionalNameStateReuse(key, nextNameState);

        String key2 = (String) transformed_inputs.get(0);
        NameState nameState2 = (NameState) transformed_inputs.get(1);
        nameState.addNextNameState(key, nextNameState);
        assertEquals(nextNameState, nameState2.getNextNameState(key2));

        // nameState.removeNextNameState("key");
        // assertNull(nameState.getNextNameState("key"));
    }

}