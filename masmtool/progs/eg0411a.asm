;eg0411a.asm
	include io32.inc
	.data
key	byte 234
buffer	byte '你能看见我吗？Can you see me?',0	
msg2	byte 'Encrypted message: ',0
msg3	byte 13,10,'Original messge: ',0
	.code
start:
	mov eax,lengthof buffer-1
	push eax	; 字符个数保存进入堆栈
	mov ecx,eax	; ECX＝实际输入的字符个数，作为循环的次数
	xor ebx,ebx	; EBX指向输入字符
encrypt:	mov al,key	; AL＝加密关键字
	xor buffer[ebx],al	; 异或加密
	inc ebx
	dec ecx	; 等同于指令：loop encrypt
	jnz encrypt	; 处理下一个字符
	mov eax,offset msg2
	call dispmsg
	mov eax,offset buffer	; 显示加密后的密文
	call dispmsg
	;
	pop ecx	; 从堆栈弹出字符个数，作为循环的次数
	xor ebx,ebx	; EBX指向输入字符
decrypt:	mov al,key	; AL＝解密关键字
	xor buffer[ebx],al	; 异或解密
	inc ebx
	dec ecx
	jnz decrypt	; 处理下一个字符
	mov eax,offset msg3
	call dispmsg
	mov eax,offset buffer	; 显示解密后的明文
	call dispmsg

	exit 0
	end start