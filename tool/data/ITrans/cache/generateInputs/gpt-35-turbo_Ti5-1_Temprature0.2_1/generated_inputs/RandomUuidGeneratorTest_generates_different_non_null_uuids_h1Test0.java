package io.cucumber.core.eventbus;

import io.cucumber.core.eventbus.UuidGenerator;
import io.cucumber.core.eventbus.UuidGenerator.*;
import org.junit.jupiter.api.Test;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class RandomUuidGeneratorTest_generates_different_non_null_uuids_h1Test0 {

    @Test
    void generates_different_non_null_uuids_h1Test0() {
        // Given
    UuidGenerator generator = new SequentialUuidGenerator();
    UuidGenerator generator2 = new SequentialUuidGenerator();
        UUID uuid1 = generator.generateId();
        // When
        UUID uuid2 = generator2.generateId();
        // Then
        assertNotEquals(uuid1, uuid2);
    }
}

