# net packet sniff 

## tcpdump(on linux)
tcpdump has pcap-filter to express packets' characteristics.
 The filter expression consists of one or more primitives.  Primitives usually consist of an id (name or number) preceded by one or more qualifiers.
       There are three different kinds of qualifier:

       type   type  qualifiers  say  what  kind of thing the id name or number refers to.  Possible types are host, net , port and portrange.  E.g., `host
              foo', `net 128.3', `port 20', `portrange 6000-6008'.  If there is no type qualifier, host is assumed.

       dir    dir qualifiers specify a particular transfer direction to and/or from id.  Possible directions are src, dst, src or dst, src  and  dst,  ra,
              ta, addr1, addr2, addr3, and addr4.  E.g., `src foo', `dst net 128.3', `src or dst port ftp-data'.  If there is no dir qualifier, src or dst
              is assumed.  The ra, ta, addr1, addr2, addr3, and addr4 qualifiers are only valid for IEEE 802.11 Wireless LAN link layers.  For  some  link
              layers, such as SLIP and the ``cooked'' Linux capture mode used for the ``any'' device and for some other device types, the inbound and out‐
              bound qualifiers can be used to specify a desired direction.

       proto  proto qualifiers restrict the match to a particular protocol.  Possible protos are: ether, fddi, tr, wlan, ip, ip6, arp, rarp,  decnet,  tcp
              and  udp.  E.g., `ether src foo', `arp net 128.3', `tcp port 21', `udp portrange 7000-7009', `wlan addr2 0:2:3:4:5:6'.  If there is no proto
              qualifier, all protocols consistent with the type are assumed.  E.g., `src foo' means `(ip or arp or rarp) src foo' (except  the  latter  is
              not legal syntax), `net bar' means `(ip or arp or rarp) net bar' and `port 53' means `(tcp or udp) port 53'.

        expr relop expr
              True  if  the  relation holds, where relop is one of >, <, >=, <=, =, !=, and expr is an arithmetic expression composed of integer constants
              (expressed in standard C syntax), the normal binary operators [+, -, *, /, %, &, |, ^, <<, >>], a length operator, and special  packet  data
              accessors.  Note that all comparisons are unsigned, so that, for example, 0x80000000 and 0xffffffff are > 0.

              The % and ^ operators are currently only supported for filtering in the kernel on Linux with 3.7 and later kernels; on all other systems, if
              those operators are used, filtering will be done in user mode, which will increase the overhead of capturing  packets  and  may  cause  more
              packets to be dropped.

              To access data inside the packet, use the following syntax:
                   proto [ expr : size ]
              Proto  is  one  of ether, fddi, tr, wlan, ppp, slip, link, ip, arp, rarp, tcp, udp, icmp, ip6 or radio, and indicates the protocol layer for
              the index operation.  (ether, fddi, wlan, tr, ppp, slip and link all refer to the link layer. radio refers to the "radio  header"  added  to
              some  802.11  captures.)   Note  that  tcp, udp and other upper-layer protocol types only apply to IPv4, not IPv6 (this will be fixed in the
              future).  The byte offset, relative to the indicated protocol layer, is given by expr.  Size is optional and indicates the number  of  bytes
              in the field of interest; it can be either one, two, or four, and defaults to one.  The length operator, indicated by the keyword len, gives
              the length of the packet.

              For example, `ether[0] & 1 != 0' catches all multicast traffic.  The expression `ip[0] & 0xf != 5' catches all IPv4  packets  with  options.
              The  expression  `ip[6:2]  & 0x1fff = 0' catches only unfragmented IPv4 datagrams and frag zero of fragmented IPv4 datagrams.  This check is
              implicitly applied to the tcp and udp index operations.  For instance, tcp[0] always means the first byte of the TCP header, and never means
              the first byte of an intervening fragment.

              Some  offsets  and  field  values  may be expressed as names rather than as numeric values.  The following protocol header field offsets are
              available: icmptype (ICMP type field), icmpcode (ICMP code field), and tcpflags (TCP flags field).

              The following ICMP type field values are available: icmp-echoreply, icmp-unreach, icmp-sourcequench, icmp-redirect, icmp-echo,  icmp-router‐
              advert,  icmp-routersolicit,  icmp-timxceed,  icmp-paramprob,  icmp-tstamp, icmp-tstampreply, icmp-ireq, icmp-ireqreply, icmp-maskreq, icmp-
              maskreply.

              The following TCP flags field values are available: tcp-fin, tcp-syn, tcp-rst, tcp-push, tcp-ack, tcp-urg.

       Primitives may be combined using:

              A parenthesized group of primitives and operators.

              Negation (`!' or `not').

              Concatenation (`&&' or `and').

              Alternation (`||' or `or').

       Negation has highest precedence.  Alternation and concatenation have equal precedence and associate left to right.  Note that explicit and  tokens,
       not juxtaposition, are now required for concatenation.




## snoop(on solaris)
### useful snoop arguments
-t [r|a|d]
Time-stamp presentation. Time-stamp are accurate to within 4 microseconds. The default is for times to be presented in d(delta) format

filter expression: expr relop expr
True if the relation holds, where relop is one of >, <, >=, <=, =, !=, and expr is an arithmetic expression composed of numbers, packet field selectors, the length primitive, and arithmetic operators +, -, *, &, |, ^, and %. The arithmetic operators within expr are evaluated before the relational operator and normal precedence rules apply between the arithmetic operators, such as multiplication before addition. Parentheses may be used to control the order of evaluation. To use the value of a field in the packet use the following syntax:
base[expr[:size]]

