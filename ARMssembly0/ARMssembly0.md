# ARMssembly0
## Description
What integer does this program print with arguments 4134207980 and 950176538? File: chall.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Solution
Compile the file and decompile the executable file with Ghidra.
```

uint max_val(uint param_1,uint param_2)
{
  if (param_2 < param_1) {
    param_2 = param_1;
  }
  return param_2;
}


int main(int argc,char **argv)

{
  uint input1;
  uint input2;
  
  input1 = atoi(argv[1]);
  input2 = atoi(argv[2]);
  input1 = max_val(input1,input2);
                    /* print the max value */
  printf("Result: %ld\n",(ulong)input1);
  return 0;
}
```

So the flag is 4134207980 in hex.

