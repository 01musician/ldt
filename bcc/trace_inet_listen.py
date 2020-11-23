from bcc import BPF

bpf_text = """
#include <net/inet_sock.h>
#include <bcc/proto.h>

int kprobe__inet_listen(struct pt_regs *ctx, struct socket *sock, int backlog)
{
    bpf_trace_printk("Listening with up to %d pending connections!\\n");
    return 0;
};
"""

b = BPF(text=bpf_text)

while True:
    print b.trace_readline()

