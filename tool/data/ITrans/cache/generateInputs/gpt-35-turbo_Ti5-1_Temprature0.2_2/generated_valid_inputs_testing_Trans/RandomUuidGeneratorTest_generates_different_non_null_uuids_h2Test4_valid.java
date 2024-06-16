package io.cucumber.core.eventbus;

import io.cucumber.core.eventbus.RandomUuidGeneratorTest_generates_different_non_null_uuids;

import io.cucumber.core.eventbus.UuidGenerator;
import io.cucumber.core.eventbus.UuidGenerator.*;
import org.junit.jupiter.api.Test;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class RandomUuidGeneratorTest_generates_different_non_null_uuids_h2Test4_valid {

    @Test
    void generates_different_non_null_uuids_h2Test4() {
        // Given
    UuidGenerator generator = new MockUuidGenerator();
    UuidGenerator generator2  = RandomUuidGeneratorTest_generates_different_non_null_uuids.inputTransformation_generates_different_non_null_uuids(generator);
        UUID uuid1 = generator.generateId();
        // When
        UUID uuid2 = generator2.generateId();
        // Then
        assertNotEquals(uuid1, uuid2);
    }
}

