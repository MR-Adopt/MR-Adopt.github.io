package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h2Test4 {

    @Test
    public void testEncryptionAndDecryption_h2Test4() {
    PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");
    String plaintext = "JAVAJAVAJAVAJAVAJAVA";
    String textTodecrypt = "ZHZHZHZHZHZH";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

