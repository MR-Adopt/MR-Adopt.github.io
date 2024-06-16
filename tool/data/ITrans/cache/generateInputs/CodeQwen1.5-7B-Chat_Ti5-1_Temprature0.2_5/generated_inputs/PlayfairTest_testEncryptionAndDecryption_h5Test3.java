package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h5Test3 {

    @Test
    public void testEncryptionAndDecryption_h5Test3() {
    PlayfairCipher playfairCipher = new PlayfairCipher("ENCRYPTION");
    String plaintext = "TESTCASE";
    String textTodecrypt = "JJJJJJJJJJ";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

