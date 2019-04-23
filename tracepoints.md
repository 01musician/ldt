# Tracepoints
## 简介
Tracepoints需要内核中有代码支持，一般部署在代码中比较重要的地方。
## Tracepoints的使用
Tracepoints的使用需要两方面的支持：
* tracepoint的定义，一般放在头文件中
* tracepoint的调用，一般在关键环节代码中调用
## Event Tracing
Event Tracing好像是在虚拟文件系统层面对Tracepoints的一个调用。
### Event Tracing的使用
