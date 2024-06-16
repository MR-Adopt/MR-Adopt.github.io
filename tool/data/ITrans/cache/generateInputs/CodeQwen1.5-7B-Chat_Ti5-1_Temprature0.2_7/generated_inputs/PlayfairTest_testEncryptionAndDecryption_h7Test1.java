package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h7Test1 {

    @Test
    public void testEncryptionAndDecryption_h7Test1() {
    PlayfairCipher playfairCipher = new PlayfairCipher("JAVA");
    String plaintext = "PROGRAMMING";
    String textTodecrypt = "JJJJJJJJJ";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

