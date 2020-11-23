# net packet sniff 

## tcpdump(on linux)


## snoop(on solaris)
### useful snoop arguments
-t [r|a|d]
Time-stamp presentation. Time-stamp are accurate to within 4 microseconds. The default is for times to be presented in d(delta) format

filter expression: expr relop expr
True if the relation holds, where relop is one of >, <, >=, <=, =, !=, and expr is an arithmetic expression composed of numbers, packet field selectors, the length primitive, and arithmetic operators +, -, *, &, |, ^, and %. The arithmetic operators within expr are evaluated before the relational operator and normal precedence rules apply between the arithmetic operators, such as multiplication before addition. Parentheses may be used to control the order of evaluation. To use the value of a field in the packet use the following syntax:
base[expr[:size]]

