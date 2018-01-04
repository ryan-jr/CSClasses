# FSU: CIS4930 - Offensive Computer Security


### Lecture 2: Secure Coding in C


* Reading: 0x260 to 0x280 in Hacking Art of Exploitation

* Intro to processors/registers

* VN Architecture, CPU, memory, Input/Output.  

* Processor has registers(Variables) EAX, EBX, ECX, EDX are main computations.  EAX -Accumulationr(usually holds return val), EBX(Accumulatior), ECX(Count/Accumulator), ESI(Used for array operands)

* EIP - Instruction poitner and pints to next instruction to be executed, and want to hijack it during exploitation, ESP = Stack pointer, EBP is the base stack pointer

* gcc.godbolt.org allows you to visualize what is being constructed/assembly

* Strings are usually the first thing that people get wrong, Strings are an array of characters up to/including the null character terminating it.  Size is the # of bytes allocated to teh array, and count is the number of elements in the array.  Size != Length (depending on character size)

* A UTF char can be 1-4 bytes wide can be 2-4 bytes.  Strings can be normal/narrow depending on normal or wide.  

* THe char types are char, unsigned, or signed char.  wchar are much the same

*  wchar_t usually uses UTF-16 and is 2 bytes(16 bits )long, whereas in Linux/OSX it usually uses UTF-32 and is thus 4bytes.  This means that a wchar_t array is not the count of the array 

* Length functions include strlen(compile time), sizeof(runtime) wcslen(for wide chars)

* String functions also may use standar C99 stuff, or POSIX/windows stuff.  Strcopy is an unbounded function that will read until the null terminating character (if there is too much info in too small a space, you can create a buffer overflow)  Buffer overflows can be caused by concatonation

* Common errors are improperly bounded string copies, off by one errors, string truncation, null termination errors (undefined behavior).  Common culprits of mem overflows are memcopy, gets, strncopy, sprintf/snprintf

* Off by one errors usually involve reading/writing outside the bounds of the array

* String truncation is when too lareg of a string is put safely into too small of a destingation, data is lost, but this can lead to a vulnerability depending on the application logic

* Failure to properly null terminate strings also reslts in errors, strncpy, snprintf, strncat don't null terminate

* Mitigations include using safe function safely, websect/unicode security guide, and using fortify source

* Pointers are also misunderstood (* and &)

* When (*) is used in declaring, a variabl instantiates a variable point to an object of a given type e.g.

```

x = &d
char *x --> char d = "ABCD"

// Basically char *x means that it will point to something that may have a number of characters

```

* Don't assume that pointers will be null, that region of memory that the pointer points to may be filled with something you don't want

* is a unary operator which denotes indirection, if the (*) doesn't point to an object/function it's behavior is undefined and *(null) will usually trigger a segfault.  

* The & is the address of operator, which is not the value that the pointer points to, but the address of the pointer itself

```

e.g. x is at 0x%08x, contains 0x%08x and it points to ABCD // This is &x, x, and *x in order


```

* The -> operator points to next operations (think list/linked list), array indexing is the next thing of arr[x] which would return the xTH element of the array

* Function pointers often are where malicious things happen because they get executed via jmp, mov, call, edi, etc...

* 32 bit versions of assembler isntructions have ebx, ecx, etc.. but 64 bit versions are appended with r

* For the global offset table, Windows/Linux use a simlar technique for linking/xfering control to library functions, linux is exploitable, windows is safe

* The GOT is part of the Executable/Linking Format (ELF) which holds absolute addresses which is essential for dynamically linked binaries.  Every library function used by a program has a GOT entry which contains addresses of the actual function, but before the first use of a library function the GOT points to the runtime linker(RTL) which is passed control and finds the functions real address and inserted into the GOT but subsequent calls don't involve the RTL

* THe GOT is located at a fixed address in very ELF, because RTL modifies the GOT it is not write protected and attackers can write to it via arbitrary memor write vuls, or redirects to shellcode.  

* GCC specifically contains .dtors which is a deconstructor for function poitners.  The constructor is .ctors and is called before main is invoked, and .dtors which is the deconstroctor is a segment, and both are writeable by default.  

* For dynamic memory managment there are memory allocation function including malloc, aligned alloc, realloc, calloc.  Malloc allocates size bytes and returns a pointer to the memory address, but memory is not zeroed.  Calloc allocates memory fo ran array elements of size bytes each and returns a pointer to the allocated memory, and the memory is set to 0

* Alignment was originally a processor design requirment, because data structure alignment is how data is arragned/access in memory.  A processor will read/write from address in word sized chunks, and alignment is putting the data at an address equal to some multiple of the word size.  You can use misaligned data but it will impact performance.  

* THere is a dynamic memory allocation in C which is not a C99 standard

* Common C mem managment erros include intilization errors, failure to check return vals, dereffing null pointers, using freed memory, multiple frees on same memory, and meory leaks

* Intilization errors is failure to zeor memory and free() does not neccessarily 0 memrory

* Failure ot check return vals, because mem can be exhaused, and a programmer might not check the return code of malloc/calloc etc.. and using a null pointer w/o checking is bad

* It is possible to access freed mem unless all pointers to that memory have been set to null or invalidated 

* Multiple frees on the same memory can be caused by cut/pase errors/sloppy error handling which can corrupt heap memory manager, and may crash/memoyr corruption vuln and/or memory leakage


* Memory Allocator is when the memory manager on most systems runs as part of the process and the linker adds in the code to do this.  OS's have default memory managers, and compilers can override/proivde alternative memory managers. 

* Dynamically linking is when things are brought in at runtime (this makes things small), static linkinking packages all of the libraries etc...   this makes the program portable

* A memory alocator is a mantained list of free/vaialbel memory, and an algo to allocate a contiguous chunk of n bytes that fits either the best fit or first fit.  These often optmize for boundries with tags for current size of chunk, size of next chunk, etc...

* Pointers such as foritify_Source with stack connaries, etc...

* Mitigations include testing, nullifying pointers after freeing them since free() does not sent pointers to null, ALSR, and testing!

* The basis of the linux mem allocator is that free chunks are arranged in a doubly linked circular list(bins) and each chunk, used/free has the next chunk and previous chunk pointers, the size of the previous chunk(if free)/ last 4 bytes of the previous used chunk (if not free), flag for if previous chunk is used/free

* In linux an allocated chunk of memory will always be larger than what was allocated because of the overhead/administrative data described above

* The system trusts the data in the "free" memory to have the correct pointers to the forward/backward free memory


```


Week 1 Reading: Hacking Art of Exploitation: 
0x200 up to 0x260 (HAOE) 
0x260 up to 0x280 (HAOE) 




Homework 1
CIS 4930 / CIS 5930
Offensive Computer Security (OCS2014)
Spring 2014

Due January 15th, 2014, by MIDNIGHT
Worth: 100 points

Electronic turn in (Turn in via email to: redwood@cs.fsu.edu) DO NOT EMAIL TO MY @fsu.edu account.  The email must be titled in the following format:
 “[OCS2014] hw1 <your last name>”. (where <your last name> is your last name)
Example:  [OCS2014] hw1 redwood

#1)  [15 points total] Visit http://www.digitalattackmap.com/ and pick out three interesting periods of activity (at the bottom).  For each provide the following [each is worth 5 points]:
The date (period)
Pick a major botnet’s activity and list:
[1 point] Source and Destination
India to worldwide including the US, Canda, Saudi Arabia, Brazil, etc...
[1 point] How long the attack has been occurring
Only about 10-15 mins or so

[2 points] How has the attack been pulled off ?  (Briefly describe and explain, not just list “Traffic Misuse”, or “SYN Flood”.  Go into a little detail).
Usually via TCP connections that are using ports other than Web, or DNS, are are often reflection based either DNS or something else predominatley.  

[1 point] Which country(s) seemed to be generating the most botnet attacks 
India and the US


#2) [15 points] Consider the disclosure debate for this question, and how in the past companies reacted hostile to vulnerability researchers disclosing vulnerabilities in their systems:
[10 points (5 each)] Pick two major companies that suffered major breaches (by hackers) and explain what happened and how they informed their customers (right away?  delayed? never? by “i’m sorry” on twitter??).  What were the consequences of the breach?  Who really was the victim?  

Target didn't notify their customers for aproximatley a week(Dec 13th shows signs of initial investigation, but only announced on Dec 19th).  After the announcement multiple class action lawsuits were filed, after Target announced 70m+ more identities stolen the next year, more class actions wer filed, Target's stock price dropped, but there was no major fluctuation in retail volumes/revenue.  Both the CEO and CIO ended up resigning, but there was no clear change in data policy/information security policy.  


[3 points] It is likely that the two companies you picked already have internal security auditing as well as contracted out penetration testing to comply with government / industry regulations.  

In many cases the regulations do not require the company enact any of the suggested security changes from the audit / test results.  For each of the above incidents do you think better regulations or better testing (or something else or nothing at all) would have helped prevent the incident? Explain for each [1.5 point each].

Better regulation may have helped, Target later announced that the data breach may have been 10+ years old, possibly affecting hundreds of millions.  So while regulation could have potentially prevented it, assuming that the regulation was strong/insightful/nuanced enough, it would also likely have mitigated it, or could have just as likely done nothing depending on how strongly enforced the regulation was. Given that information security is often overlooked/ignored, my prediction would be that such regulations would have done very little.   

[2 points] Do you think most small business or startup could afford proportional consequences?  Why or why not?

Depending on severity of backlash, most small businesses/startups likely could not support such consequences given potential negative press, loss of funding/revenue, etc...

#3) [15 points (one point each)]
What is confidentiality?
What is integrity?
What is availability?
What is a Denial of Service attack?
What is a virus?
What is a trojan?
What is a botnet?
What is a zero day?
What is a n-day?
Is a bug the same as a vulnerability?
What is a weakness?

[4 pts] Name 4 ways an attacker can act anonymously online
Spoofed MAC address, Proxy servers, hiding behind a screen name, hijacked account.  

#4)  [55 points] Read  Dan Geer’s 2013 FALL UNC CHARLOTTE CYBER SECURITY SYMPOSIUM keynote speech:  http://geer.tinho.net/geer.uncc.9x13.txt
[20 pts] What is the thesis of his talk? (Explain well)
That one of the large tradeoffs in information security is between privacy and freedom, specifically on data retention and government control.  Not only is the keynote speech titled/tagged "tradeoffs in information security", but Geer points out that one of the central questions is data, and what people/governments do with that data, how it secured, trafficed, and handled.  The theme of tradeoffs/freedom is also present in his analogy in blacklisting/whtielisting and governments.  This tradeoff is largely in the name of preventing a chatostrphic failure since society is increasingly complex.  


[5] What is your stance on the subject?

I think he starts with a flawed premise in attempting to compare governments and data.  It is possible to have specific/"heavy" regulations and still be free, e.g Capitalism still exsits  even if there were more heavy regulations on the financial sector (that could have prevented the 2008 financial crisis).


[5] What is the problem with the defensive mindset?  Do you agree?

The defender has to defend against all attacks, but the attacker only has to find one hole.  On the whole I agree, having to defend/prevent everything is a unique challenge while also struggling to maintain usability.  

[5] What aspects of the internet provide a permanent structural advantage to attackers?

Aspects such as anonimity, speed of attack, surprise, an arguably infintiely large attack surface, etc...

[5] How do biometric-based authentication systems (like the new iphone’s fingerprint password) change the debate over the 5th amendment?
[5] What are the two aspects of privacy the author discusses?
Observability and identifiability 

[5] The author asks “Is all the technologic[al] dependency and the data that fuels it making us more resilient or more fragile?”.  What do you think?
I think it makes us more fragile without proper safeguards or fallbacks.  As technology increases so does complexity, and the possibility that a basic building block that such technology is built on could fail.  

[5] Do you think you would change any of your opinions so far  if a cyber attack seriously crippled the nation’s critical infrastructure, (electric grid, water / sewer, oil & natural gas), cost many lives, and forever changed “modern society” as we know it (AKA a cyber 9/11 (a term that your instructor hates))?  If so explain.



```

***

### Lecture 3: Code Auditing

* Freeing a chunk of memory is the reversoe of malloc/memory allocation

* We want to target metadata of second chunks, since we can't write backward..  The good way to do this is to have an exploit that uses a string up to the point of metadata, and then writes into the next chunk metadata that points to an overwrite/unlink