package com.thealgorithms.ciphers;

import org.junit.jupiter.api.Test;


import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import java.util.List;
import java.util.Arrays;

public class PlayfairTest_testEncryptionAndDecryption {
    public static String inputTransformation_testEncryptionAndDecryption(PlayfairCipher playfairCipher, String plaintext)  {
        String textTodecrypt = playfairCipher.encrypt(plaintext);
        return textTodecrypt;
    }
}