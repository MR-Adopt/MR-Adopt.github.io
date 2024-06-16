package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h3Test0 {

    @Test
    public void testEncryptionAndDecryption_h3Test0() {
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVA";
    String textTodecrypt = "SHHAHRFB";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

