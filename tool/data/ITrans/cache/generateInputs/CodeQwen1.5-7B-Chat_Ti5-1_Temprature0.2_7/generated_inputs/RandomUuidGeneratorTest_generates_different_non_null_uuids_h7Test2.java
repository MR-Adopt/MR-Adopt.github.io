package io.cucumber.core.eventbus;

import io.cucumber.core.eventbus.UuidGenerator;
import io.cucumber.core.eventbus.UuidGenerator.*;
import org.junit.jupiter.api.Test;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class RandomUuidGeneratorTest_generates_different_non_null_uuids_h7Test2 {

    @Test
    void generates_different_non_null_uuids_h7Test2() {
        // Given
UuidGenerator generator = new FixedUuidGenerator(UUID.fromString("550e8400-e29b-41d4-a716-446655440000"));
UuidGenerator generator2 = new FixedUuidGenerator(UUID.fromString("550e8400-e29b-41d4-a716-446655440000"));
        UUID uuid1 = generator.generateId();
        // When
        UUID uuid2 = generator2.generateId();
        // Then
        assertNotEquals(uuid1, uuid2);
    }
}

