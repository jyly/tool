;eg0802.asm in DOS
	include io16.inc
	.data
buffer	byte 10 dup(0)	;键盘缓冲区
bufptr1	word 0	;队列头指针
bufptr2	word 0	;队列尾指针
	;按扫描码顺序给出字符的ASCII码（下档键和小写字母），不能显示的按键为0
	;第一个0不对应按键，仅用于查表指令
scantb	byte 0,1,'1234567890-=',08h	;键盘第1排的按键，从ESC到退格
	byte 0,'qwertyuiop[]',0dh	;键盘第2排的按键，从Tab到回车
	byte 0,'asdfghjkl;',27h,'`'	;键盘第3排的按键，从Ctrl到“`”符号
	byte 0,'\zxcvbnm,./',0,'*'	;键盘第4排的按键，从SHIFT到“*”符号
	byte 0,20h,0,10 dup(0)	;ALT、空格、Caps Lock和10个功能键
	byte 0,0,'789-456+1230.'	;右边小键盘，从Num Lock到Del
	.code
start:
	mov ax,@data
	mov ds,ax
	mov ax,3509h	; 获取并保存09H号原中断向量
	int 21h
	push es
	push bx
	cli	; 关中断
	push ds	; 设置09H号新中断向量
	mov ax,seg kbint
	mov ds,ax
	mov dx,offset kbint
	mov ax,2509h
	int 21h
	pop ds
	in al,21h	; 允许IRQ1中断，其他不变
	push ax
	and al,0fdh
	out 21h,al
	sti	; 开中断
start1:	call kbget	; 调用KBGET获取按键的ASCII码
	cmp al,1
	jz start2	; 是ESC键，则退出
	push ax	; 保护字符
	call dispc	; 显示字符
	pop ax	; 恢复字符
	cmp al,0dh	; 该字符是回车符吗？
	jnz start1	; 不是，则取下一个按键字符
	mov al,0ah	; 是回车符，则再进行换行
	call dispc
	jmp start1	; 继续取字符
start2:	cli	; 恢复中断屏蔽寄存器和中断向量
	pop ax
	out 21h,al
	pop dx
	pop ds
	mov ax,2509h
	int 21h
	sti

	exit 0

kbget	proc
	push bx	; 保护BX
kbget1:	cli	; 关中断，以防止对缓冲区操作时产生中断又对缓冲区操作
	mov bx,bufptr1	; 取缓冲区队列头指针
	cmp bx,bufptr2	; 与尾指针相等否？
	jnz kbget2	; 不相等，说明缓冲区有字符，转移
	sti	; 相等，说明缓冲区空，开中断
	jmp kbget1	; 等待缓冲区有字符
kbget2:	mov al,buffer[bx]	; 从队列头取得字符送AL
	inc bx	; 队列头指针增量
	cmp bx,10	; 指针是否指向队列末端？
	jc kbget3	; 没有，转移
	mov bx,0	; 指针指向队列末端，则循环，指向始端
kbget3:	mov bufptr1,bx	; 设定新的队列头指针
	sti	; 开中断
	pop bx	; 恢复BX
	ret	; 子程序返回
kbget	endp
	; KBINT中断服务程序处理09H号键盘中断
kbint	proc
	sti	; 开中断
	push ax	; 保护寄存器
	push bx
	in al,60h	; 读取键盘扫描码
	mov bl,al	; 扫描码保存在BL
	in al,61h	; 使PB7＝1，响应键盘
	or al,80h
	out 61h,al
	and al,7fh	; 使PB7＝0，允许键盘
	out 61h,al
	test bl,80h	; 键盘数据处理
	jnz kbint2	; 是断开扫描码，转KBINT2退出
	xor bh,bh
	mov al,scantb[bx]	; 是接通扫描码，转换成ASCII码
	cmp al,0	; 是否为合法的ASCII码？
	jz kbint2	; 不是，则转KBINT2退出
	mov bx,bufptr2	; 是，取队列尾指针
	mov buffer[bx],al	; 将ASCII码存入缓冲区队列尾
	inc bx	; 队列尾指针增量
	cmp bx,10	; 指针是否指向队列末端？
	jc kbint1	; 没有，转移
	mov bx,0	; 指针指向队列末端，则循环，指向始端
kbint1:	cmp bx,bufptr1	; 缓冲区是否已满？
	jz kbint2 	; 若队列满，则退出
	mov bufptr2,bx	; 队列不满，设置新的队列尾指针
kbint2:	mov al,20h	; 向中断控制器发送普通中断结束命令
	out 20h,al
	pop bx	; 恢复寄存器
	pop ax
	iret	; 中断返回
kbint	endp

	end start
