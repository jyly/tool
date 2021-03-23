;eg0307.asm
	include io32.inc
	.data
num	byte 6,7,7,8,3,0,0,0
tab	byte '67783000'
	.code
start:
	mov ecx,lengthof num
	mov esi,offset num
	mov edi,offset tab
again:	mov al,[esi]
	xchg al,[edi]
	mov [esi],al
	call dispc
	add esi,1
	add edi,1
	loop again
	xchg eax,eax
	nop

	exit 0
	end start
