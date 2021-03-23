;eg0316c.asm
	include io32.inc
	.data
srcmsg	byte 'In a major matter, no details are small.',0	
destmsg byte (lengthof srcmsg) dup (0)
	.code
start:
	xor ebx,ebx	; EBX＝0
	mov ecx,lengthof srcmsg	; ECX＝字符串长度
again:	mov al,srcmsg[ebx]	; 从源字符串取一个字符
	mov destmsg[ebx],al	; 传送到目的字符串
	inc ebx		; 指向下一个字符
	loop again	; 重复进行字符串传送

	mov eax, offset destmsg
	call dispmsg
	
	exit 0
	end start