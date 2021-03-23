;eg0316b.asm
	include io32.inc
	.data
srcmsg	byte 'In a major matter, no details are small.',0	
destmsg byte (lengthof srcmsg) dup (0)
	.code
start:
	mov esi,offset srcmsg
	mov edi,offset destmsg
	mov ecx,lengthof srcmsg

again:	mov al,[esi] 	; 从源字符串取一个字符
	mov [edi],al	; 传送到目的字符串
	add esi,1	; 地址增量
	add edi,1	; 指向下一个字符
	loop again	; 重复进行字符串传送

	mov eax, offset destmsg
	call dispmsg
	
	exit 0
	end start