## MAVLink2.0协议介绍

> *MAVLink 2*的主要新特性是：
>
> - 24 位消息 ID - 在方言中允许超过 1600 万个唯一消息定义（MAVLink 1 限制为 256）
> - [数据包签名](https://mavlink.io/en/guide/message_signing.html)- 验证消息是由可信系统发送的。
> - [消息扩展](https://mavlink.io/en/guide/define_xml_element.html#message_extensions)- 将新字段添加到现有 MAVLink 消息定义中，而不会破坏尚未更新的接收器的二进制兼容性。
> - [空字节有效载荷截断](https://mavlink.io/en/guide/serialization.html#payload_truncation)- 序列化有效载荷末尾的空（零填充）字节必须在发送前删除（所有字节都在*MAVLink 1*中发送，无论内容如何）。
> - [兼容性标志](https://mavlink.io/en/guide/serialization.html#compat_flags)/[不兼容标志](https://mavlink.io/en/guide/serialization.html#incompat_flags)- 通过指示必须以特殊/非标准方式处理的帧（具有兼容性标志的数据包仍然可以以标准方式处理，而具有不兼容标志的数据包必须如果不支持标志则丢弃）。

MAVLink2.0报文格式为：

![](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305030233775.png)

![image-20230503023419210](https://gitee.com/Duangthef1rst/drawing-bed/raw/master//202305030234242.png)

STX: 表示MAVLink帧开头的符号，在mavlink2.0中为0xfd

LEN: 消息长度，编码为1字节

INC FLAGS: 此标志位会影响报文的结构，该标志指示数据包是否包含一些特殊功能。例如标志等于0x01表示该数据包已签名，并且在数据包的末尾附加了签名

CMP FLAGS: 不影响报文的结构，即使无法解释标志，也不会阻止解析器处理消息；

SEQ: 消息顺序号，编码为1字节，取值范围为0至255

SYS ID: SYS表示系统ID，每个无人系统应该有一个唯一的系统ID，通常将系统ID 255分配给地面站

COMP ID: COMPONENT ID标识发送消息的系统组件，MAVLink 1.0中有27种硬件类型可供选择。

MSG ID: MSGID指定了载荷中嵌入的消息类型。消息ID在旧协议中是8位编码，而在新协议中是24位编码。这允许MAVLink 2.0协议中有更多的消息类型，最多达到16777215种可能性。

PAYLOAD: 位于MSG ID后面，载荷字段可以容纳多达255个字节的数据，具体取决于消息类型。

CHECKSUM: 最后两个字节是用于校验的循环冗余检查（CRC）值。整个过程可以保证消息传输过程中没有被更改，并确保发送方和接收方都具有相同的消息。

**SIGNATURE:** 签名。它是由6个字节编码的消息签名，根据完整的消息、时间戳和秘密密钥计算而来。



- 我们将MAVLink消息分为两类：状态消息和命令消息。状态消息是从无人系统发送到地面站的消息，包含有关系统状态的信息，例如其ID、位置、速度和高度。命令消息是由地面站（或用户程序）发送给无人系统以执行某些操作或由自动驾驶执行某些任务。例如，地面站可以向无人机发送命令以起飞、降落、前往航点甚至执行带有多个航点的任务。





#### **SIGNATURE**:

MAVLink 2.0使用一个可选的13个字节的签名字段来确保链接是防篡改的，从而显着提高了协议的安全性。如果不兼容性标志设置为0x01，则会附加消息的签名，以确保数据源可信。

signature包含三部分：

- LinkID，它表示用于发送数据包的链接（通道）的ID。链接或通道可以是WiFi或遥测，并且可以组合使用。每个用于发送数据的通道都应该有自己的LinkID，它提供了一种使用MAVLink 2.0进行多通道无人系统控制的手段。

- 时间戳（timestamp），它是以10微秒为单位编码的6个字节，表示自2015年1月1日GMT以来的时间。每发送一条消息，时间戳就会增加。对于每个流，时间戳被应用于元组（SystemID、ComponentID、LinkID）来定义，其中流指的是通过同一个通道传输的消息序列。时间戳用于防止重复播放攻击。
- 签名字段（signature），它是由6个字节编码的消息签名，根据完整的消息、时间戳和秘密密钥计算而来。签名包括应用于MAVLink 2.0消息（不包括签名，但包括时间戳）的SHA-256哈希的前6个字节（48位）。秘密密钥是一个32字节的共享对称密钥，存储在自动驾驶仪、地面站或MAVLink API的两端。通过这种方式，可以确保消息的完整性，以及它来自于受信任的来源。

MAVLink 2.0消息的签名对如何处理传入的MAVLink消息产生的影响。



如果消息已经签名，那么会出现以下情况：

(i)接收到的消息的时间戳比之前从相同流（由（SystemID、ComponentID、LinkID）元组标识）接收到的包要旧，则被丢弃；

(ii)接收时计算得到的签名与附加在消息上的签名不同，则可能暗示着消息中的数据被篡改；

(iii)与本地系统时间戳相比，时间戳超过一分钟。如果消息未签名，则接受/拒绝数据包的决定是实现特定的。













## Reference

https://mavlink.io/en/guide/mavlink_2.html   MAVLink 2

Micro Air Vehicle Link (MAVlink) in aNutshell: A Survey

https://mavlink.io/en/  MAVLink开发者指南