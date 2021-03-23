;eg0316.asm
	include io32.inc
	.data
srcmsg	byte 'In a major matter, no details are small.',0	
destmsg byte (lengthof srcmsg) dup (0)
	.code
start:
	mov esi,offset srcmsg
	mov edi,offset destmsg
	mov ecx,lengthof srcmsg
	cld
	rep movsb
	mov eax, offset destmsg
	call dispmsg
	
	exit 0
	end start