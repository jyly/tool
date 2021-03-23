;eg0803.asm for DOS
	include io16.inc
	.data
msg	byte 'What you see is what you get.',13,10,0
	.code
start:
	mov ax,@data
	mov ds,ax

	mov al,80h
	mov dx,2fbh
	out dx,al	;写入通信线路控制寄存器，使DLAB＝1
	mov ax,96	;分频系数：1.8432MHz÷(1200×16)＝96＝60H
	mov dx,2f8h
	out dx,al	;写入除数寄存器低8位
	mov al,ah
 	inc dx
	out dx,al	;写入除数寄存器高8位
	mov al,00001010b
	mov dx,2fbh
 	out dx,al	;写入通信线路控制寄存器
	mov al,13h	;循环测试（D4＝1） 
	mov dx,2fch	;禁止中断（D3＝0）
	out dx,al
	mov al,0	;禁止所有中断
 	mov dx,2f9h
	out dx,al	;写入中断允许寄存器（应保证此时DLAB＝0）
	;
	;读取通信线路状态，查询工作
	mov si,offset msg	; SI指向发送信息
	mov bx,1	; BX＝1表示需要发送信息
	mov cx,1	; CX＝1表示可以接收信息
statue:	mov ax,bx
	or ax,cx	; BX＝CX＝0，表示接收和发送都完成，转向结束
	jz done
	mov dx,2fdh	; 读取通信线路状态寄存器
	in al,dx
	test al,1eh	; 接收有错误否?
	jz statue1	; 没有错误，继续
	; 接收有错，响铃报警
	mov dx,2f8h	; 读出接收有误的数据，丢掉
	in al,dx
	mov al,07h	; 响铃控制的ASCII码为07H
	call dispc
	jmp statue	; 继续查询
statue1:	test al,01h	; 接收到数据吗?
	jz statue2	; 没有收到数据，继续
	; 已接收字符，读取该字符并显示（如果是结尾字符，则设置标志）
	mov dx,2f8h	; 从输入缓冲寄存器读取字符
	in al,dx
	cmp al,0	; 是结尾字符吗？ 
	jnz receive
	xor cx,cx	; CX＝0，不再接收数据
	jmp statue	; 继续查询
receive:	and al,7fh	; 传送标准ASCII码，采用7个数据位，所以仅取低7位
	call dispc	; 屏幕显示该数据
	jmp statue	; 继续查询
statue2:	cmp bx,1	; 有需要发送的字符吗？
	jne statue	; 无发送字符，继续查询
	test al,20h	; 保持寄存器空（能输出数据）吗?
	jz statue	; 不能输出，继续查询
	; 保持寄存器已空，可以发送数据
	mov al,[si]	; 获得要发送的字符
	inc si
	cmp al,0	; 是结尾字符吗？
	jnz transmit 
	xor bx,bx	; 无发送字符，设置BX＝0
	jmp statue	; 继续查询
transmit:	mov dx,2f8h	; 将字符输出给发送保持寄存器
	out dx,al	; 串行发送数据
	jmp statue	; 继续查询
done:		
	exit 0
	end start
