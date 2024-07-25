# UTF-8 Validation

This project contains a Python function `validUTF8` that determines if a given dataset represents a valid UTF-8 encoding.

## UTF-8 Encoding

UTF-8 is a variable-width character encoding used for electronic communication. Each character in UTF-8 can be represented by 1 to 4 bytes. The structure of the bytes is as follows:

1. **1-byte character**:
   - Bits: `0xxxxxxx`
2. **2-byte character**:
   - Bits: `110xxxxx 10xxxxxx`
3. **3-byte character**:
   - Bits: `1110xxxx 10xxxxxx 10xxxxxx`
4. **4-byte character**:
   - Bits: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

The first byte in a multi-byte sequence indicates the number of bytes in the character. Each subsequent byte must start with the bits `10`.

## Function Implementation

The function `validUTF8(data)` checks if the given dataset is a valid UTF-8 encoding.

### Code

```python
def validUTF8(data):
    """Determine if a given dataset represents a valid UTF-8 encoding"""
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check that the byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
