### HAOE notes


```C

// Example C function

int factorial(int x)
{
 int i;
 for(i=1; i < x; i++)
 x *= i;
 return x;
}


// Example of a function prototype
// Function prototypes tell the complie to expect a function with a name, return type, and argument type, even if that function is located at the end of a program 

 int factorial(int);

```


* Code can't do anything until it's compiled into an executable binary


* Assmbly langauge instructions have a direct 1 to 1 relationship w/ their corresponding machine language instructions, meaning htat since very processor architecture has different machine language instructions, each also has a different form of assembly language.  

* Assembly language syntax comes in either AT&T syntax or Intel Syntax, Linux usues AT&T syntax which has % and $ everywhere.  

* Much like books are writen using a limited character set/alphabet, so too are programs written with few assembly instructions using CPU variables/registers

* EAX, ECX, EDX, and EBX are all general purpose registers known as the accumulator, counter, data, and base registers respectively.  

* The ESP, EBP, ESI, and EDI registers are also known as indicies/pointers(Stack pointer, Base Pointer, Stack Index, Destination Index).  

* ESP and EBP are pointers because they store addresses/memory locations

* The EIP register is the instruction pointer which points to the current instruction the proccessor is reading and is important in debugging.  

* The EFLAGS register is used for bit flags that are used for memory comparisons/memory segmentations.  



```

Now that GDB is configured to use Intel syntax, let’s begin understanding
it. The assembly instructions in Intel syntax generally follow this style:

operation <destination>, <source>
The destination and source values will either be a register, a memory address, or a value. The operations are usually intuitive mnemonics: The mov operation will move a value from the source to the destination, sub will subtract, inc will increment, and so forth. For example, the instructions below will move the value from ESP to EBP and then subtract 8 from ESP (storing the result in ESP).

8048375: 89 e5 mov ebp,esp
8048377: 83 ec 08 sub esp,0x8

```

* GDB uses a variety of commands including info register eip which would be expressed as (i r eip at the GDP command prompt)

* The other useful command is x/(o octal, x, hex, u, unsigned int, t, binary)

* A function prolouge is gnerated to set up memory for th erest of the main functions local variables, etc...


```

 the display units for the examine command can be changed by adding a
size letter to the end of the format letter. The valid size letters are as follows:
b A single byte
h A halfword, which is two bytes in size
w A word, which is four bytes in size
g A giant, which is eight bytes in size
Programming 29
This is slightly confusing, because sometimes the term word also refers to
2-byte values. In this case a double word or DWORD refers to a 4-byte value. In this
book, words and DWORDs both refer to 4-byte values. If I’m talking about a
2-byte value, I’ll call it a short or a halfword. The following GDB output shows
memory displayed in various sizes.
(gdb) x/8xb $eip
0x8048384 <main+16>: 0xc7 0x45 0xfc 0x00 0x00 0x00 0x00 0x83
(gdb) x/8xh $eip
0x8048384 <main+16>: 0x45c7 0x00fc 0x0000 0x8300 0xfc7d 0x7e09 0xeb02 0xc713
(gdb) x/8xw $eip
0x8048384 <main+16>: 0x00fc45c7 0x83000000 0x7e09fc7d 0xc713eb02
0x8048394 <main+32>: 0x84842404 0x01e80804 0x8dffffff 0x00fffc45
(gdb)
If you look closely, you may notice something odd about the data above.
The first examine command shows the first eight bytes, and naturally, the
examine commands that use bigger units display more data in total. However,
the first examine shows the first two bytes to be 0xc7 and 0x45, but when a
halfword is examined at the exact same memory address, the value 0x45c7 is
shown, with the bytes reversed. This same byte-reversal effect can be seen
when a full four-byte word is shown as 0x00fc45c7, but when the first four bytes
are shown byte by byte, they are in the order of 0xc7, 0x45, 0xfc, and 0x00.
This is because on the x86 processor values are stored in little-endian
byte order, which means the least significant byte is stored first. For example,
if four bytes are to be interpreted as a single value, the bytes must be used
in reverse order. The GDB debugger is smart enough to know how values
are stored, so when a word or halfword is examined, the bytes must be
reversed to display the correct values in hexadecimal

```





* A string is technically a charactar array.  

* An array is a list of n elements of a (specific) data type

* Arrays are also known as buffers

* 