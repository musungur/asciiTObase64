# asciiTObase64
Base64 is a binary to Text conversion -enabling transmission/serialization of data in an obfuscated text(8bits ascii binary representation of character To 6bits of binary representation of a character).<br />
Ascii - is data encoding from text(human readable ) to binary represantaion(Machine readable). Data is transmitted on the medium(ethernet/wireless/fiber) in binary form. Ascii represents a single character with (8bits),which is 1 byte. A standard ascii which was written for alphanumeric(english characters), represent a character with 8bits. The Most significant Bit(MSB) is always a zero(0) reserved for standard ascii, thus a character is a seven bit. A standard ascii ranges from 0 - 127 numbers that can be representation of binary code pints. Code point is a calculated representation of a binary into a decimal number that is stored in the memory(for which an inode mapps to a character that is output to a graphical character on a screen.<br />

Unlike ascii which is intended for conversion of: human readable text to machine readable binary(8bits per character) for transmission/serialization on a medium,and to their code point in memory storage, Base64 is intended for reversing ascii process by converting ascii binary(8bits) to Text(a 6bits character text) for transmission on a medium.<br/>
How does Base64 works: (Base64 represents binary in 6bits per character (unlike 8bits per character for ascii)).<br />
<b span="Base64 calc">Example</b>
1. Take an standard ascii binary number, i.e: code point 65, in binary (0100 0001) represents character 'A' in binary decimal.to convert to Base64, you devide the bits into 6bits per character starting from Left to right. when bits becomes less, you add zeros.<br /><hr />
  <b>ascii (01000001) = code point 65 = A; = base64 (010000 010000) = code point = 32 = g ( from base64 table binary 01000001 has been converted to base64 text 'g'.</b>
  <hr />
