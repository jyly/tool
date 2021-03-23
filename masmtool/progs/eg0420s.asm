;eg0420s.asm（子程序文件）
	include io32.inc
	public read, write, mean	; 子程序共用
	extern temp:dword	; 外部变量
	.data
writebuf	byte 12 dup(0)	; 显示缓冲区
readbuf		byte 30 dup(0)

	.code
write	proc c	; 显示有符号十进制数的子程序，EAX＝入口参数
	push ebx	; 保护寄存器
	push ecx
	push edx
	mov ecx,sizeof writebuf-1	; 显示缓冲区清0
write0:	mov writebuf[ecx],0
	sub ecx,1
	jnc write0
	mov ebx,offset writebuf	; EBX指向显示缓冲区
	test eax,eax	; 判断数据是零、正数或负数
	jnz write1	; 不是零，跳转
	mov byte ptr [ebx],'0'	; 是零，设置"0"
	jmp write5	; 转向显示
write1:	jns write2	; 是正数，跳转
	mov byte ptr [ebx],'-'	; 是负数，设置负号"－"
	inc ebx
	neg eax	; 数据求补（绝对值）
write2:	mov ecx,10
	push ecx	; 10压入堆栈，作为退出标志
write3:	cmp eax,0	; 数据（商）为零，转向保存
	jz write4 
	xor edx,edx	; 零位扩展被除数为EDX.EAX
	div ecx	; 数据除以10：EDX.EAX÷10
	add edx,30h	; 余数（0～9）转换为ASCII码
	push edx	; 数据各位先低位后高位压入堆栈
	jmp write3
write4:	pop edx	; 数据各位先高位后低位弹出堆栈
	cmp edx,ecx	; 是结束标志10，转向显示
	je write5
	mov [ebx],dl	; 数据保存到缓冲区
	inc ebx
	jmp write4
write5:	mov eax,offset writebuf
	call dispmsg
	pop edx	; 恢复寄存器
	pop ecx
	pop ebx
	ret	; 子程序返回
write	endp

read	proc c	; 输入有符号十进制数的子程序
	push eax	; 出口参数：变量TEMP＝补码表示的二进制数值
	push ebx	; 说明：负数用"－"引导
	push ecx
	push edx
read0:	mov eax,offset readbuf
	call readmsg	; 输入一个字符串
	test eax,eax
	jz readerr	; 没有输入数据，转向错误处理
	cmp eax,12
	ja readerr	; 输入超过12个字符，转向错误处理
	mov edx,offset readbuf	; EDX指向输入缓冲区
	xor ebx,ebx	; EBX保存结果
	xor ecx,ecx	; ECX为正负标志，0为正，－1为负
	mov al,[edx]	; 取一个字符
	cmp al,'+'	; 是"＋"，继续
	jz read1
	cmp al,'-'	; 是"－"，设置－1标志
	jnz read2
	mov ecx,-1
read1:	inc edx	; 取下一个字符
	mov al,[edx]
	test al,al	; 是结尾0，转向求补码
	jz read3
read2:	cmp al,'0'	; 不是0～9之间的数码，则输入错误
	jb readerr
	cmp al,'9'
	ja readerr
	sub al,30h	; 是0～9之间的数码，则转换为二进制数
	imul ebx,10	; 原数值乘10：EBX＝EBX×10
	jc readerr	; CF＝1，说明乘积溢出，输入数据超出32位范围，出错
	movzx eax,al	; 零位扩展，便于相加
	add ebx,eax	; 原数值乘10后，与新数码相加
	jnc read1	; CF＝0，继续转换下一个数位
		; CF＝1，说明输入数据超出32位范围，出错
readerr:	mov eax,offset errmsg
	call dispmsg
	jmp read0
	;
read3:	test ecx,ecx	; 判断是正数还是负数
	jz read4
	cmp ebx,80000000h	; 负数超过231，出错
	ja readerr
	neg ebx	; 是负数，进行求补
	jmp read5
read4:	cmp ebx,7fffffffh	; 正数超过231-1，出错
	ja readerr
read5:	mov temp,ebx	; 设置出口参数
	pop edx
	pop ecx
	pop ebx
	pop eax
	ret	; 子程序返回
errmsg	byte 'Input error, enter again: ',0
read	endp

mean	proc c	; 计算32位有符号数平均值子程序
	push ebp	; 入口参数：顺序压入数据个数和数组偏移地址
	mov ebp,esp	; 出口参数：EAX＝平均值
	push ebx	; 保护寄存器
	push ecx
	push edx
	mov ebx,[ebp+8]	; EBX＝堆栈中取出的偏移地址
	mov ecx,[ebp+12]	; ECX＝堆栈中取出的数据个数
	xor eax,eax	; EAX保存和值
	xor edx,edx	; EDX＝指向数组元素
mean1:	add eax,[ebx+edx*4]	; 求和
	add edx,1	; 指向下一个数据
	cmp edx,ecx	; 比较个数
	jb mean1	; 循环
	cdq	; 将累加和EAX符号扩展到EDX
	idiv ecx	; 有符号数除法，EAX＝平均值（余数在EDX中）
	pop edx	; 恢复寄存器
	pop ecx
	pop ebx
	pop ebp
	ret
mean	endp

	end
