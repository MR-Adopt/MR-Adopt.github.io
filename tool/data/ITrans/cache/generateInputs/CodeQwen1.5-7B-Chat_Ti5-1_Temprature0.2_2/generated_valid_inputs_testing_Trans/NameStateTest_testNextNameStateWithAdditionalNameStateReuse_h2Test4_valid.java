package software.amazon.event.ruler;

import software.amazon.event.ruler.NameStateTest_testNextNameStateWithAdditionalNameStateReuse;

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

public class NameStateTest_testNextNameStateWithAdditionalNameStateReuse_h2Test4_valid {

    @Test
    public void testNextNameStateWithAdditionalNameStateReuse_h2Test4() {
    NameState nameState = new NameState();
    NameState nextNameState = new NameState();
    String key = "key";
		List<Object> transformed_inputs = NameStateTest_testNextNameStateWithAdditionalNameStateReuse.inputTransformation_testNextNameStateWithAdditionalNameStateReuse(key, nextNameState);
    String key2  = (String) transformed_inputs.get(0);
    NameState nameState2  = (NameState) transformed_inputs.get(1);
    nextNameState.addNextNameState(key, nextNameState);
    nameState.addNextNameState(key, nextNameState);
        nameState.addNextNameState(key, nextNameState);
        assertEquals(nextNameState, nameState2.getNextNameState(key2));
    // nameState.removeNextNameState("key");
    // assertNull(nameState.getNextNameState("key"));
    }
}

